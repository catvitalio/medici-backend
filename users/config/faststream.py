from faststream import FastStream
from faststream.rabbit import RabbitBroker

from config.settings import settings
from events.info import router as info_router
from events.login import router as login_router
from events.register import router as register_router

broker = RabbitBroker(settings.RMQ_URI.unicode_string())
broker.include_router(register_router)
broker.include_router(info_router)
broker.include_router(login_router)

app = FastStream(broker)
