from http import HTTPStatus

from pydantic import BaseModel


class RabbitSyncErrorDTO(BaseModel):
    message: str
    status_code: HTTPStatus
