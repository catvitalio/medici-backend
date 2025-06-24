from pydantic import AmqpDsn, PostgresDsn
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    POSTGRES_URI: PostgresDsn
    RMQ_URI: AmqpDsn


settings = Settings()  # type: ignore
