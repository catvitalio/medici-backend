from decimal import Decimal
from typing import TYPE_CHECKING

from sqlalchemy import DECIMAL, Enum, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from constants import AccountType, Bank, CryptoCurrency, Currency
from constants.money import MONEY_PRECISION, MONEY_SCALE
from .base import Base

if TYPE_CHECKING:
    from .transaction import Transaction


class BankAccount(Base):
    bank: Mapped[Bank] = mapped_column(Enum(Bank), nullable=False)
    currency: Mapped[Currency] = mapped_column(Enum(Currency), nullable=False)

    account_id: Mapped[int] = mapped_column(Integer, nullable=False)
    account: Mapped['Account'] = relationship(back_populates='bank_account')


class CashAccount(Base):
    currency: Mapped[Currency] = mapped_column(Enum(Currency), nullable=False)

    account_id: Mapped[int] = mapped_column(Integer, nullable=False)
    account: Mapped['Account'] = relationship(back_populates='cash_account')


class CryptoAccount(Base):
    currency: Mapped[CryptoCurrency] = mapped_column(
        Enum(CryptoCurrency),
        nullable=False,
    )

    account_id: Mapped[int] = mapped_column(Integer, nullable=False)
    account: Mapped['Account'] = relationship(back_populates='crypto_account')


class Account(Base):
    user_id: Mapped[int] = mapped_column(Integer, nullable=False)
    name: Mapped[str] = mapped_column(String, nullable=False)
    balance: Mapped[Decimal] = mapped_column(
        DECIMAL(MONEY_PRECISION, MONEY_SCALE),
        nullable=False,
        default=Decimal(0),
    )
    account_type: Mapped[AccountType] = mapped_column(Enum(AccountType), nullable=False)

    transactions: Mapped[list['Transaction']] = relationship(back_populates='account')
    bank_account: Mapped[BankAccount | None] = relationship(back_populates='account')
    cash_account: Mapped[CashAccount | None] = relationship(back_populates='account')
    crypto_account: Mapped[CryptoAccount | None] = relationship(
        back_populates='account',
    )
