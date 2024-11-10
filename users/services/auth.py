from faststream import Depends
from sqlalchemy import select
from sqlalchemy.exc import NoResultFound
from sqlalchemy.ext.asyncio import AsyncSession

from config.security import hasher
from deps import get_db
from dtos import AuthDTO
from exceptions import InvalidCredentials
from models import User


class AuthService:
    def __init__(self, db: AsyncSession = Depends(get_db)) -> None:
        self._db = db

    async def auth(self, dto: AuthDTO) -> User:
        user = await self._get_user(dto.email)
        if not hasher.verify(dto.password, user.hashed_password):
            raise InvalidCredentials

        return user

    async def _get_user(self, email: str) -> User:
        stmt = select(User).where(User.email == email)
        user = await self._db.execute(stmt)

        try:
            return user.scalar_one()
        except NoResultFound:
            raise InvalidCredentials
