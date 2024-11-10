from pydantic import BaseModel


class AuthDTO(BaseModel):
    email: str
    password: str
