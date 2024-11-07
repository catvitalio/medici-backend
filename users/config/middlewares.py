from faststream import Context, ExceptionMiddleware
from faststream.rabbit import RabbitBroker
from faststream.rabbit.message import RabbitMessage

from exceptions import DirectReplyToException

exc_middleware = ExceptionMiddleware()


@exc_middleware.add_handler(Exception)
async def direct_reply_to_exc_handler(
    exc: Exception,
    broker: RabbitBroker = Context(),
    message: RabbitMessage = Context(),
) -> None:
    if message.reply_to and isinstance(exc, DirectReplyToException):
        await broker.publish(
            {
                'message': exc.message,
                'status_code': exc.status_code,
            },
            message.reply_to,
            correlation_id=message.correlation_id,
        )


middlewares = (exc_middleware,)
