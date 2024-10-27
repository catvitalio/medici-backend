from faststream.rabbit.fastapi import RabbitRouter

from .settings import settings

queue_router = RabbitRouter(settings.RMQ_URI.unicode_string())
