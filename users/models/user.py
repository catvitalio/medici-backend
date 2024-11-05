from models.base import Base

from sqlalchemy import Boolean, String
from sqlalchemy.orm import Mapped, mapped_column


class User(Base):
    email: Mapped[str] = mapped_column(String, unique=True, index=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(String, nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
