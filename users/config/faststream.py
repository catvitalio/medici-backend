from faststream import FastStream
from faststream.rabbit import RabbitBroker

from events.register import router as users_router
from .settings import settings

broker = RabbitBroker(settings.RMQ_URI.unicode_string())
broker.include_router(users_router)

app = FastStream(broker)
