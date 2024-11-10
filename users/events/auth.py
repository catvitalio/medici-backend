from faststream import Depends
from faststream.rabbit import RabbitRouter

from dtos import AuthDTO, UserDTO
from services import AuthService

router = RabbitRouter()


@router.subscriber('user.auth.command')
async def auth(dto: AuthDTO, service: AuthService = Depends(AuthService)) -> UserDTO:
    user = await service.auth(dto)
    return UserDTO.model_validate(user, from_attributes=True)
