from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session, joinedload
from app.database import get_db
from app.models.scholarships import Scholarships as Scholarship
from app.models.saved_scholarships import SavedScholarship
from app.models.user import User
from app.core.jwt import SECRET_KEY
from jose import jwt, JWTError
from datetime import date

router = APIRouter()


@router.get("/scholarships")
def get_all_scholarships(
    request: Request,
    db: Session = Depends(get_db)
):

    today = date.today()

    # ----------------------------
    # 1️⃣ Try to extract user (if token exists)
    # ----------------------------
    current_user = None
    print("Authorization Header:", request.headers.get("Authorization"))
    
    auth_header = request.headers.get("Authorization")
    
    if auth_header and auth_header.startswith("Bearer "):
        token = auth_header.split(" ")[1]

        try:
            payload = jwt.decode(
                token,
                SECRET_KEY,
                algorithms=["HS256"]
            )

            user_id = payload.get("sub")

            if user_id:
                current_user = (
                    db.query(User)
                    .filter(User.id == user_id)
                    .first()
                )

        except JWTError:
            pass  # Ignore invalid token


    # ----------------------------
    # 2️⃣ Fetch all active scholarships
    # ----------------------------
    scholarships = (
        db.query(Scholarship)
        .filter(Scholarship.status == "active")
        .options(joinedload(Scholarship.eligibility))
        .all()
    )

    print("Current User:", current_user)
    # ----------------------------
    # 3️⃣ Fetch saved scholarship IDs (Optimized)
    # ----------------------------
    saved_ids = set()

    if current_user:
        saved_query = (
            db.query(SavedScholarship.scholarship_id)
            .filter(SavedScholarship.user_id == current_user.id)
            .all()
        )

        saved_ids = {row[0] for row in saved_query}


    # ----------------------------
    # 4️⃣ Build Response
    # ----------------------------
    result = []

    for sch in scholarships:

        eligibility_list = [
            {
                "domicile_state": elig.domicile_state,
                "category": elig.category,
                "gender": elig.gender,
                "family_income_max": elig.family_income_max,
                "course_stream": elig.course_stream,
                "education_level": elig.education_level,
            }
            for elig in sch.eligibility
        ]

        result.append({
            "scholarship_id": sch.scholarship_id,
            "scholarship_name": sch.scholarship_name,
            "provider_name": sch.provider_name,
            "provider_type": sch.provider_type,
            "benefit_type": sch.benefit_type,
            "benefit_amount": sch.benefit_amount,
            "application_end_date": sch.application_end_date,
            "description": sch.description,
            "is_featured": sch.is_featured,
            "priority_score": sch.priority_score,
            "eligibility": eligibility_list,
            "is_saved": sch.scholarship_id in saved_ids  # ✅ Safe check
        })

    return result