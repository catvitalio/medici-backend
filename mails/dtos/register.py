from pydantic import BaseModel


class RegisterStartedDTO(BaseModel):
    id: int  # noqa: A003
    email: str
    is_active: bool
    token: str
