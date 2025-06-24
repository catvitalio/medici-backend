from models import Transaction
from .abc import AbstractRepository


class TransactionRepository(AbstractRepository):
    model = Transaction
