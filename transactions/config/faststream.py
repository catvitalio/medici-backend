from faststream import FastStream
from faststream.rabbit import RabbitBroker

from config.settings import settings

broker = RabbitBroker(settings.RMQ_URI.unicode_string())

app = FastStream(broker)
