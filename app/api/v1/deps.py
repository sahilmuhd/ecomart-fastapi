from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.db.models.user import User
from app.db.models.tenant import Tenant

def get_current_user(db: Session = Depends(get_db), user_id: int = Depends(get_current_user_id)) -> User:
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user

def get_current_user_id():
    # Logic to retrieve the current user ID from the request context
    pass

def get_current_tenant(db: Session = Depends(get_db), tenant_id: int = Depends(get_current_tenant_id)) -> Tenant:
    tenant = db.query(Tenant).filter(Tenant.id == tenant_id).first()
    if not tenant:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tenant not found")
    return tenant

def get_current_tenant_id():
    # Logic to retrieve the current tenant ID from the request context
    pass