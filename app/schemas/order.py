from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class OrderItem(BaseModel):
    product_id: int
    quantity: int
    price: float

class OrderCreate(BaseModel):
    items: List[OrderItem]
    total_amount: float
    shipping_address: str

class OrderUpdate(BaseModel):
    items: Optional[List[OrderItem]] = None
    total_amount: Optional[float] = None
    shipping_address: Optional[str] = None

class Order(BaseModel):
    id: int
    items: List[OrderItem]
    total_amount: float
    shipping_address: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True