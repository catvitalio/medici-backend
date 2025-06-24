from enum import Enum


class Bank(str, Enum):
    TINKOFF = 'tinkoff'
    SBER = 'sber'
    ALFA = 'alfa'
