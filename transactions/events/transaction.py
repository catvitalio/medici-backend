from faststream import Depends
from faststream.rabbit import RabbitRouter

from dtos import (
    TransactionCreateDTO,
    TransactionListDTO,
    TransactionListParamsDTO,
)
from services import TransactionListService

router = RabbitRouter()


@router.subscriber('transaction.list.query')
async def get_list(
    dto: TransactionListParamsDTO,
    service: TransactionListService = Depends(TransactionListService),
) -> TransactionListDTO:
    return await service.get_list(dto)


@router.subscriber('transaction.create.command')
async def create(dto: TransactionCreateDTO) -> None:
    ...
