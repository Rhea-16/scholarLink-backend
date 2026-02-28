from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal

from app.models.user_profile import Profile
from app.schemas.registration import ProfileCreate
from app.core.jwt import get_current_user   # if using JWT

router = APIRouter(    
    prefix="/profile",
    tags=["Profile"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register")
def create_profile(
    profile: ProfileCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)   # remove if no JWT yet
):
    db_profile = Profile(
        user_id=current_user["user_id"],
        **profile.model_dump()
    )

    db.add(db_profile)
    db.commit()
    db.refresh(db_profile)

    return {"message": "Profile created successfully"}
