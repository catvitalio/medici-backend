from pydantic import BaseModel


class AuthDTO(BaseModel):
    email: str
    password: str


class TokenPairDTO(BaseModel):
    access: str
    refresh: str


class RefreshDTO(BaseModel):
    token: str
