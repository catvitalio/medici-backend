from faststream import Depends
from faststream.rabbit import RabbitRouter
from sqlalchemy.ext.asyncio import AsyncSession

from deps import get_db
from dtos import RegisterDTO, UserDTO
from services import RegisterService

router = RabbitRouter('users.')


@router.subscriber('register')
@router.publisher('register')
async def register(dto: RegisterDTO, db: AsyncSession = Depends(get_db)) -> UserDTO:
    service = RegisterService(db)
    user = await service.register(dto)
    return UserDTO(user)
