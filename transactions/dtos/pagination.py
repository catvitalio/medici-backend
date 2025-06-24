from pydantic import BaseModel


class PaginationDTO(BaseModel):
    limit: int
    offset: int


class PaginatedDTO(BaseModel):
    limit: int
    offset: int
    total: int
    items: list
