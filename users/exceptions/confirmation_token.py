class ConfirmationTokenError(Exception):
    message = 'Confirmation token error'


class InvalidToken(ConfirmationTokenError):
    message = 'Invalid confirmation token'
