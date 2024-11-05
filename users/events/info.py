from models.user import User

from faststream import Depends
from faststream.rabbit import RabbitRouter
from sqlalchemy.ext.asyncio import AsyncSession

from deps.db import get_db
from dtos import UserDTO

router = RabbitRouter()


@router.subscriber('user.info.query')
@router.publisher('user.info.result')
async def get_info(user_id: int, db: AsyncSession = Depends(get_db)) -> UserDTO:
    user = await db.get(User, user_id)
    return UserDTO.model_validate(user)
