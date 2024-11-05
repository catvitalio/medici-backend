from fastapi import APIRouter

from config.faststream import broker
from dtos import RegisterStartDTO
from dtos.register import RegisterCompleteDTO

router = APIRouter()


@router.post('/register')
async def start(dto: RegisterStartDTO) -> None:
    async with broker:
        await broker.publish(dto, 'user.register_start.command')


@router.post('/register/complete')
async def complete(dto: RegisterCompleteDTO) -> None:
    async with broker:
        await broker.publish(dto, 'user.register_complete.command')
