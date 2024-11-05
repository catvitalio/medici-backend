import asyncio
from email.message import EmailMessage

from config.jinja import jinja_env
from config.settings import settings
from config.smtp import smtp_client
from dtos import SendMailDTO


class SendMailService:
    @classmethod
    async def send(cls, dto: SendMailDTO) -> None:
        messages = cls._get_messages(dto)
        asyncio.gather(*[cls._handle_message(message) for message in messages])

    @staticmethod
    def _get_messages(dto: SendMailDTO) -> list[EmailMessage]:
        messages = []
        content = jinja_env.get_template(dto.template).render(**dto.context)

        for recipient in dto.to:
            message = EmailMessage()
            message['Subject'] = dto.subject
            message['From'] = settings.SMTP_FROM
            message['To'] = recipient
            message.add_header('Content-Type', 'text/html')
            message.set_payload(content, 'utf-8')
            messages.append(message)

        return messages

    @staticmethod
    async def _handle_message(message: EmailMessage) -> None:
        async with smtp_client:
            await smtp_client.send_message(message)
