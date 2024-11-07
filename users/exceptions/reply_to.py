from http import HTTPStatus


class ReplyToException(Exception):
    message: str
    status_code: HTTPStatus = HTTPStatus.INTERNAL_SERVER_ERROR
