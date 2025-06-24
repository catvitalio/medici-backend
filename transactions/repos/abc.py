from abc import ABC
from typing import Any, Generic, TypeVar

from sqlalchemy import ColumnExpressionArgument
from sqlalchemy.ext.asyncio import AsyncSession

from models import Base

ModelT = TypeVar('ModelT', bound=Base)


class AbstractRepository(ABC, Generic[ModelT]):
    model: type[ModelT]

    def __init__(self, db: AsyncSession) -> None:
        self._db = db

    async def count(
        self,
        limit: int | None = None,
        offset: int | None = None,
        *filters: ColumnExpressionArgument,
    ) -> int:
        ...

    async def get_list(
        self,
        limit: int | None = None,
        offset: int | None = None,
        *filters: ColumnExpressionArgument,
    ) -> list[ModelT]:
        ...

    async def _select(
        self,
        limit: int | None = None,
        offset: int | None = None,
        *filters: ColumnExpressionArgument,
    ) -> list[ModelT]:
        ...

    async def create(self, obj: ModelT) -> ModelT:
        ...

    async def update(self, obj: ModelT) -> ModelT:
        ...

    async def delete(self, obj: ModelT) -> None:
        ...

    async def update_where(
        self,
        data: dict[str, Any],
        *filters: ColumnExpressionArgument,
    ) -> None:
        ...

    async def delete_where(self, *filters: ColumnExpressionArgument) -> None:
        ...

    async def bulk_create(self, objs: list[ModelT]) -> None:
        ...

    async def bulk_update(self, objs: list[ModelT]) -> None:
        ...
