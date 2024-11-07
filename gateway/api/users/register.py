from fastapi import APIRouter, Depends, HTTPException
from faststream.rabbit import RabbitBroker

from deps.broker import get_broker
from dtos import DirectReplyToErrorDTO, RegisterCompleteDTO, RegisterStartDTO, UserDTO

router = APIRouter(prefix='/users/register', tags=['users'])


@router.post('/start')
async def start(dto: RegisterStartDTO, broker: RabbitBroker = Depends(get_broker)) -> UserDTO:
    msg = await broker.request(dto, 'user.register_start.command')
    body = await msg.decode()

    try:
        return UserDTO.model_validate(body, from_attributes=True)
    except ValueError:
        error = DirectReplyToErrorDTO.model_validate(body)
        raise HTTPException(status_code=error.status_code, detail=error.message)


@router.post('/complete')
async def complete(dto: RegisterCompleteDTO, broker: RabbitBroker = Depends(get_broker)) -> UserDTO:
    msg = await broker.request(dto, 'user.register_complete.command')
    body = await msg.decode()

    try:
        return UserDTO.model_validate(body, from_attributes=True)
    except ValueError:
        raise HTTPException(status_code=400, detail=body)
