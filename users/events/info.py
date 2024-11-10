from faststream import Depends
from faststream.rabbit import RabbitRouter
from sqlalchemy.ext.asyncio import AsyncSession

from deps import get_db
from dtos import UserDTO, UserInfoDTO
from models import User

router = RabbitRouter()


@router.subscriber('user.info.query')
@router.publisher()
async def get_info(dto: UserInfoDTO, db: AsyncSession = Depends(get_db)) -> UserDTO:
    user = await db.get(User, dto.id)
    return UserDTO.model_validate(user, from_attributes=True)
