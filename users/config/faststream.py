from faststream import FastStream
from faststream.rabbit import RabbitBroker

from config.middlewares import middlewares
from config.settings import settings
from events.auth import router as auth_router
from events.info import router as info_router
from events.register import router as register_router

broker = RabbitBroker(settings.RMQ_URI.unicode_string(), middlewares=middlewares)
broker.include_router(auth_router)
broker.include_router(info_router)
broker.include_router(register_router)

app = FastStream(broker)
