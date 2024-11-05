from faststream import FastStream
from faststream.rabbit import RabbitBroker

from config.settings import settings
from events.register import router as register_router

broker = RabbitBroker(settings.RMQ_URI.unicode_string())
broker.include_router(register_router)

app = FastStream(broker)
