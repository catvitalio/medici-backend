from pydantic import BaseModel, EmailStr


class RegisterStartDTO(BaseModel):
    email: EmailStr
    password: str


class RegisterCompleteDTO(BaseModel):
    token: str
