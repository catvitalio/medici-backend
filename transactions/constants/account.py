from enum import Enum


class AccountType(str, Enum):
    BANK = 'bank'
    CASH = 'cash'
    CRYPTO = 'crypto'
