from typing import Generic, TypeVar

from fastapi import HTTPException
from faststream.rabbit import RabbitBroker
from pydantic import BaseModel

from dtos import RabbitSyncErrorDTO

ReplyT = TypeVar('ReplyT', bound=BaseModel)


class RabbitSyncClient(Generic[ReplyT]):
    """
    RabbitMQ sync client with validation and error handling.
    Implemented via direct reply-to feature.
    """

    def __init__(self, broker: RabbitBroker) -> None:
        self._broker = broker

    async def send(self, body: BaseModel, reply_type: type[ReplyT], topic: str) -> ReplyT:
        msg = await self._broker.request(body, topic)
        reply_body = await msg.decode()

        try:
            return reply_type.model_validate(reply_body, from_attributes=True)
        except ValueError:
            error = RabbitSyncErrorDTO.model_validate(reply_body)
            raise HTTPException(status_code=error.status_code, detail=error.message)
