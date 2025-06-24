from decimal import Decimal

from pydantic import BaseModel

from constants import Bank, CryptoCurrency, Currency
from .pagination import PaginatedDTO, PaginationDTO


class BankAccountDTO(BaseModel):
    id: int  # noqa: A003
    bank: Bank
    currency: Currency


class CashAccountDTO(BaseModel):
    id: int  # noqa: A003
    currency: Currency


class CryptoAccountDTO(BaseModel):
    id: int  # noqa: A003
    currency: CryptoCurrency


class TransactionDTO(BaseModel):
    id: int  # noqa: A003
    amount: Decimal
    account: BankAccountDTO | CashAccountDTO | CryptoAccountDTO
    user_id: int


class TransactionListParamsDTO(PaginationDTO):
    user_id: int
    account_id: int | None


class TransactionListDTO(PaginatedDTO):
    items: list[TransactionDTO]


class TransactionCreateDTO(BaseModel):
    user_id: int
    account_id: int
    amount: Decimal
