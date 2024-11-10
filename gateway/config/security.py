from fastapi import Request
from fastapi.security import OAuth2PasswordBearer

from exceptions import NotAuthenticated


class OAuth2CookiePasswordBearer(OAuth2PasswordBearer):
    async def __call__(self, request: Request) -> str | None:
        headers_auth = request.headers.get('Authorization')
        if headers_auth:
            return await super().__call__(request)

        cookie_token = request.cookies.get('access_token')
        if not cookie_token:
            if self.auto_error:
                raise NotAuthenticated
            else:
                return

        return cookie_token


bearer_security = OAuth2CookiePasswordBearer(tokenUrl='/api/auth')
