from fastapi import APIRouter, Depends, HTTPException
from app.schemas.user import UserCreate, UserOut
from app.services.auth_service import AuthService
from app.db.models.user import User
from app.db.session import get_db
from sqlalchemy.orm import Session

router = APIRouter()

@router.post("/register", response_model=UserOut)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = AuthService.get_user_by_email(db, email=user.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return AuthService.create_user(db=db, user=user)

@router.post("/login", response_model=UserOut)
def login_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = AuthService.authenticate_user(db, email=user.email, password=user.password)
    if not db_user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return db_user