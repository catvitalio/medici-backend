from faststream import Context, ExceptionMiddleware
from faststream.rabbit import RabbitBroker
from faststream.rabbit.message import RabbitMessage

from exceptions import ReplyToException

exc_middleware = ExceptionMiddleware()


@exc_middleware.add_handler(Exception)
async def reply_to_handler(
    exc: Exception,
    broker: RabbitBroker = Context(),
    message: RabbitMessage = Context(),
) -> None:
    if message.reply_to and isinstance(exc, ReplyToException):
        await broker.publish(
            {
                'message': exc.message,
                'status_code': exc.status_code,
            },
            message.reply_to,
            correlation_id=message.correlation_id,
        )


middlewares = (exc_middleware,)
