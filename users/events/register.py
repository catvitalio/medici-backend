from faststream import Depends
from faststream.rabbit import RabbitRouter

from dtos import RegisterCompleteDTO, RegisterStartDTO, RegisterStartedDTO, UserDTO
from services import RegisterService

router = RabbitRouter()


@router.subscriber('user.register_start.command')
@router.publisher('user.register_started.event')
async def start(
    dto: RegisterStartDTO,
    service: RegisterService = Depends(RegisterService),
) -> RegisterStartedDTO:
    return await service.start(dto)


@router.subscriber('user.register_complete.command')
async def complete(
    dto: RegisterCompleteDTO,
    service: RegisterService = Depends(RegisterService),
) -> UserDTO:
    user = await service.complete(dto)
    return UserDTO.model_validate(user, from_attributes=True)
