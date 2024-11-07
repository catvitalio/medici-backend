from fastapi import Depends
from faststream.rabbit import RabbitBroker

from services import RabbitSyncClient
from .broker import get_broker


def get_sync_client(broker: RabbitBroker = Depends(get_broker)) -> RabbitSyncClient:
    return RabbitSyncClient(broker)
