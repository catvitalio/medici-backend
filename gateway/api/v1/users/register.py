from config.fastapi import api_router
from config.faststream import queue_router


@api_router.post('/register')
@queue_router.publisher('register')
async def register(data):
    ...
