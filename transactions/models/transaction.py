from decimal import Decimal
from typing import TYPE_CHECKING

from sqlalchemy import DECIMAL, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from constants import MONEY_PRECISION, MONEY_SCALE
from models.base import Base

if TYPE_CHECKING:
    from .account import Account
    from .category import Category


class Transaction(Base):
    amount: Mapped[Decimal] = mapped_column(
        DECIMAL(MONEY_PRECISION, MONEY_SCALE),
        nullable=False,
    )

    account: Mapped['Account'] = relationship(back_populates='transactions')
    account_id: Mapped[int] = mapped_column(Integer, nullable=False)
    category: Mapped['Category'] = relationship(back_populates='transactions')
    category_id: Mapped[int] = mapped_column(Integer, nullable=False)
