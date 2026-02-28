from pydantic import BaseModel
from datetime import date
from decimal import Decimal
from typing import Optional, Literal

class ProfileResponse(BaseModel):
    profile_id: int
    user_id: str

    first_name: str
    middle_name: Optional[str] = None
    last_name: str
    dob: date
    email: Optional[str] = None

    gender: Literal["male", "female", "other"]
    religion: Optional[str] = None
    caste: Optional[str] = None
    category: Literal["general", "obc", "sc", "st", "ews", "minority"]

    nationality: Optional[str] = "Indian"

    specially_abled: bool = False
    is_orphan: bool = False
    is_minority: bool = False

    state: str
    district: Optional[str] = None
    city: str
    taluka: Optional[str] = None
    pincode: str

    primary_phone: str
    secondary_phone: Optional[str] = None

    school_name: Optional[str] = None
    tenth_pass_year: Optional[int] = None
    tenth_percentage: Optional[Decimal] = None

    is_twelfth_passed: bool = False
    college_name: Optional[str] = None
    twelfth_pass_year: Optional[int] = None
    twelfth_percentage: Optional[Decimal] = None

    is_diploma_student: bool = False

    family_income: Decimal
    family_members_count: Optional[int] = None

    family_farmer: bool = False
    family_covid_victim: bool = False
    family_military: bool = False

    class Config:
        from_attributes = True  # pydantic v2 (use orm_mode=True if v1)