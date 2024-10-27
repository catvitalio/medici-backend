from faststream.rabbit import RabbitRouter

from dtos import SendMailDTO
from services import SendMailService

router = RabbitRouter('mails.')


@router.subscriber('send_mail')
async def send_mail(dto: SendMailDTO) -> None:
    await SendMailService().send(dto)
