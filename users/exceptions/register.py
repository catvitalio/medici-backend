from http import HTTPStatus

from .reply_to import ReplyToException


class RegisterException(ReplyToException):
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
