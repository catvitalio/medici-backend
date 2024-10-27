from pydantic import AmqpDsn
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    RMQ_URI: AmqpDsn


settings = Settings()  # type: ignore
