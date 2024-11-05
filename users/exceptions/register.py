class RegisterException(Exception):
    message = 'Register error'


class UserWithThisEmailAlreadyExists(RegisterException):
    message = 'User with this email already exists'


class UserNotFound(RegisterException):
    message = 'User not found'


class UserAlreadyActive(RegisterException):
    message = 'User already active'
