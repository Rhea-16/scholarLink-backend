from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.user_profile import Profile
from app.schemas.profile_schema import ProfileResponse
from app.core.jwt import get_current_user  # your JWT dependency

router = APIRouter(prefix="/profile", tags=["Profile"])

@router.get("/me", response_model=ProfileResponse)
def get_my_profile(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    # current_user can be ORM object or dict depending on your auth code
    user_id = getattr(current_user, "user_id", None) or current_user.get("user_id")

    profile = db.query(Profile).filter(Profile.user_id == user_id).first()
    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found")

    return profile