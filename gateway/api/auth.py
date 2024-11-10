from fastapi import APIRouter, Depends, Response, status

from dtos import AuthDTO, RefreshDTO
from services import AuthService

router = APIRouter(prefix='/auth', tags=['auth'])


@router.post('', status_code=status.HTTP_204_NO_CONTENT)
async def auth(dto: AuthDTO, service: AuthService = Depends()) -> Response:
    pair = await service.auth(dto)
    return service.get_response_with_cookies(pair)


@router.post('/refresh', status_code=status.HTTP_204_NO_CONTENT)
def refresh(dto: RefreshDTO, service: AuthService = Depends()) -> Response:
    pair = service.refresh_tokens(dto.token)
    return service.get_response_with_cookies(pair)


@router.post('/logout', status_code=status.HTTP_204_NO_CONTENT)
def logout(service: AuthService = Depends()) -> Response:
    return service.get_response_with_cookies(None)
