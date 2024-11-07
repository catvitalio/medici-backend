from faststream import Depends
from faststream.rabbit import RabbitRouter
from sqlalchemy.ext.asyncio import AsyncSession

from deps import get_db
from dtos import RegisterCompleteDTO, RegisterStartDTO, UserDTO
from services import RegisterService

router = RabbitRouter()


@router.subscriber('user.register_start.command')
@router.publisher('user.register_started.event')
@router.publisher()
async def start(dto: RegisterStartDTO, db: AsyncSession = Depends(get_db)) -> UserDTO:
    service = RegisterService(db)
    user = await service.start(dto)
    return UserDTO.model_validate(user, from_attributes=True)


@router.subscriber('user.register_complete.command')
@router.publisher('user.register_completed.event')
@router.publisher()
async def complete(dto: RegisterCompleteDTO, db: AsyncSession = Depends(get_db)) -> UserDTO:
    service = RegisterService(db)
    user = await service.complete(dto)
    return UserDTO.model_validate(user, from_attributes=True)
