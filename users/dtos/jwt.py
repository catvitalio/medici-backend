from pydantic import BaseModel


class TokenPairDTO(BaseModel):
    access: str
    refresh: str
