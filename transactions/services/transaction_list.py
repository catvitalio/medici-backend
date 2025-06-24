from faststream import Depends
from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from deps import get_db
from dtos.transaction import (
    TransactionDTO,
    TransactionListDTO,
    TransactionListParamsDTO,
)
from models import Transaction


class TransactionListService:
    def __init__(self, db: AsyncSession = Depends(get_db)) -> None:
        self._db = db

    async def get_list(self, dto: TransactionListParamsDTO) -> TransactionListDTO:
        return TransactionListDTO(
            limit=dto.limit,
            offset=dto.offset,
            total=await self._get_total(dto),
            items=await self._get_items(dto),
        )

    async def _get_total(self, dto: TransactionListParamsDTO) -> int:
        stmt = (
            select(func.count(Transaction.id))
            .join(Transaction.account)
            .where(Transaction.account.user_id == dto.user_id)
        )
        if dto.account_id is not None:
            stmt = stmt.where(Transaction.account_id == dto.account_id)

        return await self._db.execute(stmt)

    async def _get_items(self, dto: TransactionListParamsDTO) -> list[TransactionDTO]:
        stmt = (
            select(Transaction)
            .join(Transaction.account)
            .where(Transaction.account.user_id == dto.user_id)
            .limit(dto.limit)
            .offset(dto.offset)
        )
        if dto.account_id is not None:
            stmt = stmt.where(Transaction.account_id == dto.account_id)

        return TransactionDTO.model_dump(await self._db.execute(stmt))
