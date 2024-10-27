from pydantic import AmqpDsn, EmailStr
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    RMQ_URI: AmqpDsn

    SMTP_HOSTNAME: str
    SMTP_PORT: int
    SMTP_USERNAME: EmailStr
    SMTP_PASSWORD: str
    SMTP_FROM: EmailStr
    SMTP_START_TLS: bool
    SMTP_USE_TLS: bool


settings = Settings()  # type: ignore
