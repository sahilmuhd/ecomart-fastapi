from pydantic import BaseModel
from typing import Optional

class StoreBase(BaseModel):
    name: str
    description: Optional[str] = None
    owner_id: int

class StoreCreate(StoreBase):
    pass

class StoreUpdate(StoreBase):
    pass

class Store(StoreBase):
    id: int

    class Config:
        orm_mode = True