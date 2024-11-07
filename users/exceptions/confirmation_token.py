from http import HTTPStatus

from .direct_reply_to import DirectReplyToException


class ConfirmationTokenException(DirectReplyToException):
    message = 'Confirmation token error'


class InvalidToken(ConfirmationTokenException):
    message = 'Invalid confirmation token'
    status_code = HTTPStatus.FORBIDDEN
