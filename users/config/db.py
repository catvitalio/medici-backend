from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from .settings import settings

session_factory: type[AsyncSession] = sessionmaker(
    create_async_engine(settings.POSTGRES_URI.unicode_string()),  # type: ignore
    expire_on_commit=False,
    class_=AsyncSession,
)  # type: ignore
