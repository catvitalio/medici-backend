from typing import NamedTuple


class MailType(NamedTuple):
    subject: str
    template: str


mail_type_map = {
    'register': MailType('Подтверждение регистрации', 'register.html'),
}
