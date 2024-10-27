from pydantic import BaseModel, EmailStr, Field, field_validator

from constants import MailType, mail_type_map


class SendMailDTO(BaseModel):
    to: list[EmailStr]
    type: MailType  # noqa: A003
    context: dict = Field(default_factory=dict)

    @field_validator('type', mode='before')
    def get_type(cls, v: str) -> MailType:
        return mail_type_map[v]
