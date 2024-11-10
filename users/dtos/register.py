from pydantic import BaseModel, EmailStr


class RegisterStartDTO(BaseModel):
    email: EmailStr
    password: str


class RegisterStartedDTO(BaseModel):
    id: int  # noqa: A003
    email: EmailStr
    is_active: bool
    token: str


class RegisterCompleteDTO(BaseModel):
    token: str
