from datetime import timedelta

from faststream import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from config.security import hasher
from deps import get_db
from dtos import RegisterCompleteDTO, RegisterStartDTO
from exceptions.register import (
    UserAlreadyActive,
    UserByTokenNotFound,
    UserWithThisEmailAlreadyExists,
)
from models import User
from services.confirmation_token import ConfirmationTokenService


class RegisterService:
    TOKEN_TTL = timedelta(days=365)

    def __init__(self, db: AsyncSession = Depends(get_db)) -> None:
        self._db = db
        self._token_service = ConfirmationTokenService(self.TOKEN_TTL)

    async def start(self, dto: RegisterStartDTO) -> User:
        await self._validate_user(dto)
        return await self._create_user(dto)

    async def _validate_user(self, dto: RegisterStartDTO) -> None:
        user = await self._get_user(dto.email, is_active=True)
        if user:
            raise UserWithThisEmailAlreadyExists

    async def _create_user(self, dto: RegisterStartDTO) -> User:
        user = await self._get_user(dto.email, is_active=False)
        if not user:
            user = User(
                email=dto.email,
                hashed_password=hasher.hash(dto.password),
                is_active=False,
            )
            self._db.add(user)
            await self._db.commit()
            await self._db.refresh(user)

        return user

    async def _get_user(self, email: str, *, is_active: bool) -> User | None:
        results = await self._db.execute(
            select(User).where(User.email == email, User.is_active == is_active),
        )
        return results.scalar_one_or_none()

    async def complete(self, dto: RegisterCompleteDTO) -> User:
        user_id = self._token_service.decode(dto.token)
        user = await self._db.get(User, int(user_id))

        if not user:
            raise UserByTokenNotFound
        elif user.is_active:
            raise UserAlreadyActive

        user.is_active = True
        await self._db.commit()

        return user
