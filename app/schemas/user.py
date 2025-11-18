from pydantic import BaseModel, EmailStr
from typing import Optional

class UserBase(BaseModel):
    email: EmailStr
    full_name: str
    username: str

class UserOut(BaseModel):
    id: int
    email: str
    is_active: bool = True
    model_config = {"from_attributes": True}

class UserCreate(BaseModel):
    email: str
    password: str

class UserUpdate(UserBase):
    password: Optional[str] = None

class UserInDB(UserBase):
    hashed_password: str

class User(UserBase):
    id: int

    class Config:
        orm_mode = True