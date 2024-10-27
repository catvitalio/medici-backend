from pydantic import BaseModel


class UserDTO(BaseModel):
    id: int  # noqa: A003
    email: str
