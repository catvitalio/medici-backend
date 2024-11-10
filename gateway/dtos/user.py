from pydantic import BaseModel


class UserInfoDTO(BaseModel):
    id: int  # noqa: A003


class UserDTO(BaseModel):
    id: int  # noqa: A003
    email: str
    is_active: bool
