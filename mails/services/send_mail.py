from email.message import EmailMessage

from config.jinja import jinja_env
from config.settings import settings
from config.smtp import smtp_client
from dtos import SendMailDTO


class SendMailService:
    async def send(self, dto: SendMailDTO) -> None:
        """
        Send mails to recipients

        Additionally, the SMTP protocol is not designed to be used in parallel. Multiple commands
        must be sent to send an email, and they must be sent in the correct sequence. As a
        consequence of this, executing multiple SMTP.send_message() tasks in parallel
        (i.e. with asyncio.gather()) is not any more efficient than executing in sequence, as the
        client must wait until one mail is sent before beginning the next.

        https://aiosmtplib.readthedocs.io/en/latest/client.html
        """
        async with smtp_client:
            messages = await self._get_messages(dto)
            for message in messages:
                await smtp_client.send_message(message)

    async def _get_messages(self, dto: SendMailDTO) -> list[EmailMessage]:
        messages = []
        content = jinja_env.get_template(dto.type.template).render(**dto.context)

        for recipient in dto.to:
            message = EmailMessage()
            message['Subject'] = dto.type.subject
            message['From'] = settings.SMTP_FROM
            message['To'] = recipient
            message.add_header('Content-Type', 'text/html')
            message.set_payload(content, 'utf-8')
            messages.append(message)

        return messages
