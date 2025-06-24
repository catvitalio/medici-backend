from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from config.settings import settings

engine = create_async_engine(settings.POSTGRES_URI.unicode_string())
session_factory: type[AsyncSession] = sessionmaker(
    engine,  # type: ignore
    expire_on_commit=False,
    class_=AsyncSession,
)  # type: ignore
