from pydantic import AmqpDsn, SecretStr
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    RMQ_URI: AmqpDsn
    SECRET_KEY: SecretStr


settings = Settings()  # type: ignore
