from http import HTTPStatus

from pydantic import BaseModel


class DirectReplyToErrorDTO(BaseModel):
    message: str
    status_code: HTTPStatus
