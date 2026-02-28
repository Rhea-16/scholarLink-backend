from pydantic import BaseModel, EmailStr
from datetime import date
from typing import Optional
from decimal import Decimal

class ProfileCreate(BaseModel):

    # Basic Info
    first_name: str
    middle_name: Optional[str] = None
    last_name: str
    dob: date
    gender: str
    religion: Optional[str] = None
    caste: Optional[str] = None
    category: str
    nationality: Optional[str] = "Indian"

    # Social Flags
    specially_abled: Optional[bool] = False
    is_orphan: Optional[bool] = False
    is_minority: Optional[bool] = False

    # Address
    state: str
    district: Optional[str] = None
    city: str
    taluka: Optional[str] = None
    pincode: str

    # Contact
    primary_phone: str
    secondary_phone: Optional[str] = None
    email: Optional[EmailStr] = None

    # Academic – 10th
    school_name: Optional[str] = None
    tenth_pass_year: Optional[int] = None
    tenth_percentage: Optional[Decimal] = None

    # Academic – 12th
    is_twelfth_passed: Optional[bool] = False
    college_name: Optional[str] = None
    twelfth_pass_year: Optional[int] = None
    twelfth_percentage: Optional[Decimal] = None

    # Diploma
    is_diploma_student: Optional[bool] = False

    # Family Info
    family_income: Decimal
    family_members_count: Optional[int] = None
    family_farmer: Optional[bool] = False
    family_covid_victim: Optional[bool] = False
    family_military: Optional[bool] = False
