from pydantic import BaseModel

class TenantBase(BaseModel):
    name: str
    description: str

class TenantCreate(TenantBase):
    pass

class TenantUpdate(TenantBase):
    pass

class Tenant(TenantBase):
    id: int

    class Config:
        orm_mode = True