from fastapi import Depends

from config.security import OAuth2CookiePasswordBearer, bearer_security
from dtos.user import UserDTO
from services.jwt import JWTService


def get_current_user(
    token: OAuth2CookiePasswordBearer = Depends(bearer_security),
    service: JWTService = Depends(),
) -> UserDTO:
    return service.decode(token)  # type: ignore
