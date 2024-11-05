from faststream.rabbit import RabbitRouter

from dtos import SendMailDTO, UserDTO
from services import SendMailService

router = RabbitRouter()


@router.subscriber('user.register_started.event')
async def register(dto: UserDTO) -> None:
    mail_dto = SendMailDTO(
        to=[dto.email],
        template='register.html',
        subject='Подтверждение регистрации',
        context={
            'link': 'https://medici.com/confirm-email',
        },
    )
    await SendMailService.send(mail_dto)
