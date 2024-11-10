from fastapi import status

from .declarative import DeclarativeHTTPException


class AuthException(DeclarativeHTTPException):
    detail = 'Auth error'
    status_code = status.HTTP_401_UNAUTHORIZED


class InvalidCredentials(AuthException):
    detail = 'Invalid credentials'


class NotAuthenticated(AuthException):
    detail = 'Not authenticated'
