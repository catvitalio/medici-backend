from fastapi import APIRouter, Depends, Response

from dtos import AuthDTO, RefreshDTO
from services import AuthService

router = APIRouter(prefix='/auth', tags=['auth'])


@router.post('')
async def auth(dto: AuthDTO, service: AuthService = Depends()) -> Response:
    pair = await service.auth(dto)
    return service.get_response_with_cookies(pair)


@router.post('/refresh')
def refresh(dto: RefreshDTO, service: AuthService = Depends()) -> Response:
    pair = service.refresh_tokens(dto.token)
    return service.get_response_with_cookies(pair)


@router.post('/logout')
def logout(service: AuthService = Depends()) -> Response:
    return service.get_response_with_cookies(None)
