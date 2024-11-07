from http import HTTPStatus

from .reply_to import ReplyToException


class ConfirmationTokenException(ReplyToException):
    message = 'Confirmation token error'


class InvalidToken(ConfirmationTokenException):
    message = 'Invalid confirmation token'
    status_code = HTTPStatus.FORBIDDEN
