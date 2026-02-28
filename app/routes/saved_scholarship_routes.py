from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import and_
from typing import List

from app.database import get_db
from app.models.saved_scholarships import SavedScholarship
from app.models.scholarships import Scholarships
from app.models.user import User
from app.core.jwt import get_current_user  


router = APIRouter(prefix="/saved", tags=["Saved Scholarships"])

@router.post("/{scholarship_id}")
def save_scholarship(
    scholarship_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    # Check if already saved
    existing = db.query(SavedScholarship).filter(
        and_(
            SavedScholarship.user_id == current_user["user_id"],
            SavedScholarship.scholarship_id == scholarship_id
        )
    ).first()

    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Scholarship already saved"
        )

    new_save = SavedScholarship(
        user_id=current_user["user_id"],
        scholarship_id=scholarship_id
    )

    db.add(new_save)
    db.commit()

    return {"message": "Scholarship saved successfully"}

@router.delete("/{scholarship_id}")
def unsave_scholarship(
    scholarship_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    saved = db.query(SavedScholarship).filter(
        and_(
            SavedScholarship.user_id == current_user["user_id"],
            SavedScholarship.scholarship_id == scholarship_id
        )
    ).first()

    if not saved:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Scholarship not found in saved list"
        )

    db.delete(saved)
    db.commit()

    return {"message": "Scholarship removed successfully"}

@router.get("/")
def get_saved_scholarships(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    saved_scholarships = (
        db.query(Scholarships)
        .join(
            SavedScholarship,
            Scholarships.scholarship_id == SavedScholarship.scholarship_id
        )
        .filter(SavedScholarship.user_id == current_user["user_id"])
        .all()
    )

    return saved_scholarships