from typing import AsyncGenerator

from faststream.rabbit import RabbitBroker

from config.faststream import broker


async def get_broker() -> AsyncGenerator[RabbitBroker, None]:
    async with broker:
        yield broker
