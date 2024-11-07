from http import HTTPStatus


class DirectReplyToException(Exception):
    message: str
    status_code: HTTPStatus = HTTPStatus.INTERNAL_SERVER_ERROR
