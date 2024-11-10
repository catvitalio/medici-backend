from fastapi import APIRouter, Depends

from deps import get_current_user
from dtos import RegisterCompleteDTO, RegisterStartDTO, UserDTO, UserInfoDTO
from services import RabbitSyncClient

router = APIRouter(prefix='/users', tags=['users'])


@router.get('/me')
async def me(
    user: UserDTO = Depends(get_current_user),
    client: RabbitSyncClient = Depends(),
) -> UserDTO:
    return await client.send(UserInfoDTO(id=user.id), UserDTO, 'user.info.query')


@router.post('/register/start')
async def register_start(dto: RegisterStartDTO, client: RabbitSyncClient = Depends()) -> UserDTO:
    return await client.send(dto, UserDTO, 'user.register_start.command')


@router.post('/register/complete')
async def register_complete(
    dto: RegisterCompleteDTO,
    client: RabbitSyncClient = Depends(),
) -> UserDTO:
    return await client.send(dto, UserDTO, 'user.register_complete.command')
