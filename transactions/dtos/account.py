from pydantic import BaseModel


class AccountDTO(BaseModel):
    id: int  # noqa: A003
    name: str
