import asyncio
from email.message import EmailMessage

from config.jinja import jinja_env
from config.settings import settings
from config.smtp import smtp_client
from dtos import SendMailDTO


class SendMailService:
    async def send(self, dto: SendMailDTO) -> None:
        messages = self._get_messages(dto)
        asyncio.gather(*[self._handle_message(message) for message in messages])

    def _get_messages(self, dto: SendMailDTO) -> list[EmailMessage]:
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

    async def _handle_message(self, message: EmailMessage) -> None:
        async with smtp_client:
            await smtp_client.send_message(message)
