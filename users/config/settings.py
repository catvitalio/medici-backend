from pydantic import AmqpDsn, PostgresDsn, SecretStr
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    POSTGRES_URI: PostgresDsn
    RMQ_URI: AmqpDsn
    SECRET_KEY: SecretStr


settings = Settings()  # type: ignore
