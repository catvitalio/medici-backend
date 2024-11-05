from pydantic import BaseModel, EmailStr, Field


class SendMailDTO(BaseModel):
    to: list[EmailStr]
    template: str
    subject: str
    context: dict = Field(default_factory=dict)
