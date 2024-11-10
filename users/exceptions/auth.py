from http import HTTPStatus

from .reply_to import ReplyToException


class AuthException(ReplyToException):
    message = 'Authentication error'


class InvalidCredentials(AuthException):
    message = 'Invalid credentials'
    status_code = HTTPStatus.UNAUTHORIZED
