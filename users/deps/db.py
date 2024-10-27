from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession

from config.db import session_factory


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with session_factory() as session:
        yield session
