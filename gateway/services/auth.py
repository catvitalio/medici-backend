from fastapi import Depends, Response, status
from jose import JWTError

from dtos import AuthDTO, TokenPairDTO, UserDTO
from exceptions import InvalidCredentials
from services import JWTService, RabbitSyncClient


class AuthService:
    def __init__(self, client: RabbitSyncClient = Depends()) -> None:
        self._token_service = JWTService()
        self._client = client

    async def auth(self, dto: AuthDTO) -> TokenPairDTO:
        user = await self._client.send(dto, UserDTO, 'user.auth.command')
        return self.obtain_tokens(user)

    def obtain_tokens(self, user: UserDTO) -> TokenPairDTO:
        return self._token_service.obtain(user)

    def refresh_tokens(self, token: str) -> TokenPairDTO:
        try:
            return self._token_service.refresh(token)
        except JWTError:
            raise InvalidCredentials

    @staticmethod
    def get_response_with_cookies(pair: TokenPairDTO | None) -> Response:
        response = Response(status_code=status.HTTP_204_NO_CONTENT)
        response.set_cookie('access_token', pair.access if pair else '', httponly=True)
        response.set_cookie('refresh_token', pair.refresh if pair else '', httponly=True)
        return response
