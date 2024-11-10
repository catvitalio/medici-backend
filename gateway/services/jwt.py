from datetime import datetime, timedelta

from jose import jwt
from jose.constants import ALGORITHMS
from jose.exceptions import ExpiredSignatureError, JWTError

from config.settings import settings
from dtos import TokenPairDTO, UserDTO
from exceptions import InvalidCredentials, SignatureExpired


class JWTService:
    def __init__(
        self,
        access_ttl: timedelta = timedelta(minutes=15),
        refresh_ttl: timedelta = timedelta(days=30),
        secret: str = settings.SECRET_KEY.get_secret_value(),
        algorithm: str = ALGORITHMS.HS256,
    ) -> None:
        self._access_ttl = access_ttl
        self._refresh_ttl = refresh_ttl
        self._secret = secret
        self._algorithm = algorithm

    def obtain(self, user: UserDTO) -> TokenPairDTO:  # noqa: A002
        return TokenPairDTO(
            access=self.encode(user, self._access_ttl),
            refresh=self.encode(user, self._refresh_ttl),
        )

    def refresh(self, token: str) -> TokenPairDTO:
        try:
            sub = jwt.decode(token, self._secret, algorithms=self._algorithm)['sub']
        except ExpiredSignatureError:
            raise SignatureExpired
        except JWTError:
            raise InvalidCredentials

        return TokenPairDTO(
            access=self.encode(sub, self._access_ttl),
            refresh=self.encode(sub, self._refresh_ttl),
        )

    def encode(self, user: UserDTO | dict, ttl: timedelta) -> str:  # noqa: A002
        user = UserDTO.model_validate(user)

        return jwt.encode(
            {
                'sub': str(user.id),
                'email': user.email,
                'is_active': user.is_active,
                'exp': datetime.now() + ttl,
            },
            self._secret,
            algorithm=self._algorithm,
        )

    def decode(self, token: str) -> UserDTO:
        try:
            payload = jwt.decode(token, self._secret, algorithms=self._algorithm)
        except ExpiredSignatureError:
            raise SignatureExpired
        except JWTError:
            raise InvalidCredentials

        return UserDTO(
            id=payload['sub'],
            email=payload['email'],
            is_active=payload['is_active'],
        )
