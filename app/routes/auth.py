from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal

from app.models.user import User
from app.schemas.auth import UserSignup
from app.schemas.auth import UserLogin
from app.core.security import hash_password
from app.core.security import verify_password
from app.core.jwt import create_access_token

router = APIRouter(prefix="/auth", tags=["Auth"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/signUp")
def signUp_user(user: UserSignup, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already exists")

    if not user.phone:
        raise HTTPException(status_code=400, detail="Phone number is required")

    new_user = User(
        email=user.email,
        full_name=f"{user.first_name} {user.last_name}",
        hashed_password=hash_password(user.password),
        phone=user.phone
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    # 🔑 AUTO-LOGIN: generate JWT
    access_token = create_access_token(
        data={"sub": new_user.id}
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }


@router.post("/login")
def login_user(credentials: UserLogin, db: Session = Depends(get_db)):
    # 1. Find user by email
    user = db.query(User).filter(User.email == credentials.email).first()
    print(user.email if user else "No user found")
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    # 2. Verify password
    if not verify_password(credentials.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    # 3. Create JWT token
    access_token = create_access_token(
        data={"sub": user.id}
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }
