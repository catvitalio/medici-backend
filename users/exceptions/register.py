from http import HTTPStatus

from .direct_reply_to import DirectReplyToException


class RegisterException(DirectReplyToException):
    message = 'Register error'


class UserWithThisEmailAlreadyExists(RegisterException):
    message = 'User with this email already exists'
    status_code = HTTPStatus.BAD_REQUEST


class UserByTokenNotFound(RegisterException):
    message = 'User by token not found'
    status_code = HTTPStatus.BAD_REQUEST


class UserAlreadyActive(RegisterException):
    message = 'User already active'
    status_code = HTTPStatus.BAD_REQUEST
