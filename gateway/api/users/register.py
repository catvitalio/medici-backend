from fastapi import APIRouter, Depends

from deps import get_sync_client
from dtos import RegisterCompleteDTO, RegisterStartDTO, UserDTO
from services import RabbitSyncClient

router = APIRouter(prefix='/users/register', tags=['users'])


@router.post('/start')
async def start(
    dto: RegisterStartDTO,
    client: RabbitSyncClient = Depends(get_sync_client),
) -> UserDTO:
    return await client.send(dto, UserDTO, 'user.register_start.command')


@router.post('/complete')
async def complete(
    dto: RegisterCompleteDTO,
    client: RabbitSyncClient = Depends(get_sync_client),
) -> UserDTO:
    return await client.send(dto, UserDTO, 'user.register_complete.command')
