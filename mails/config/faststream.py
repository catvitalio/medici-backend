from faststream import FastStream
from faststream.rabbit import RabbitBroker

from events.send_mail import router as send_mail_router
from .settings import settings

broker = RabbitBroker(settings.RMQ_URI.unicode_string())
broker.include_router(send_mail_router)

app = FastStream(broker)
