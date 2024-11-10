from faststream import Depends
from faststream.rabbit import RabbitRouter

from config.settings import settings
from dtos import RegisterStartedDTO, SendMailDTO
from services import SendMailService

router = RabbitRouter()


@router.subscriber('user.register_started.event')
async def register(
    dto: RegisterStartedDTO,
    service: SendMailService = Depends(SendMailService),
) -> None:
    mail_dto = SendMailDTO(
        to=[dto.email],
        template='register.html',
        subject='Подтверждение регистрации',
        context={
            'link': f'{settings.FRONTEND_URL}/confirm-email?token={dto.token}',
        },
    )
    await service.send(mail_dto)
