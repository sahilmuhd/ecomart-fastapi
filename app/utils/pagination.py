from typing import List, TypeVar, Generic
from fastapi import Query

T = TypeVar('T')

class PaginatedResponse(Generic[T]):
    items: List[T]
    total: int
    page: int
    size: int

def paginate(items: List[T], page: int = Query(1, ge=1), size: int = Query(10, ge=1)) -> PaginatedResponse[T]:
    start = (page - 1) * size
    end = start + size
    return PaginatedResponse(
        items=items[start:end],
        total=len(items),
        page=page,
        size=size
    )