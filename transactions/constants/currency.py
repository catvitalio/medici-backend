from enum import Enum


class Currency(str, Enum):
    RUB = 'RUB'
    USD = 'USD'
    EUR = 'EUR'


class CryptoCurrency(str, Enum):
    BTC = 'BTC'
    ETH = 'ETH'
    USDT = 'USDT'
