from models import User

from sqlalchemy.ext.asyncio import AsyncSession

from config.security import hasher
from dtos.register import RegisterDTO


class RegisterService:
    def __init__(self, db: AsyncSession) -> None:
        self._db = db

    async def register(self, dto: RegisterDTO) -> User:
        user = User(email=dto.email, hashed_password=hasher.hash(dto.password))
        self._db.add(user)
        await self._db.commit()
        return user
