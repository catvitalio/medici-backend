from aiosmtplib import SMTP

from .settings import settings

smtp_client = SMTP(
    hostname=settings.SMTP_HOSTNAME,
    port=settings.SMTP_PORT,
    username=settings.SMTP_USERNAME,
    password=settings.SMTP_PASSWORD,
    use_tls=settings.SMTP_USE_TLS,
    start_tls=settings.SMTP_START_TLS,
)
