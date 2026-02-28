from sqlalchemy import Column, String, BigInteger, Date, Enum, Integer, DECIMAL, Boolean, TIMESTAMP, text
from app.database import Base
import uuid

class Profile(Base):
    __tablename__ = "user_profile" 

    profile_id = Column(BigInteger, primary_key=True, autoincrement=True)
    user_id = Column(String(36), nullable=False)

    first_name = Column(String(100), nullable=False)
    middle_name = Column(String(100))
    last_name = Column(String(100), nullable=False)
    dob = Column(Date, nullable=False)
    email = Column(String(50),nullable=True)

    gender = Column(Enum('male','female','other'), nullable=False)
    religion = Column(String(50))
    caste = Column(String(100))
    category = Column(Enum('general','obc','sc','st','ews','minority'), nullable=False)

    nationality = Column(String(50), server_default="Indian")

    specially_abled = Column(Boolean, default=False)
    is_orphan = Column(Boolean, default=False)
    is_minority = Column(Boolean, default=False)

    state = Column(String(100), nullable=False)
    district = Column(String(100))
    city = Column(String(100), nullable=False)
    taluka = Column(String(36),nullable = True)
    pincode = Column(String(10), nullable=False)

    primary_phone = Column(String(15), nullable=False)
    secondary_phone = Column(String(15))

    school_name = Column(String(255))
    tenth_pass_year = Column(Integer)
    tenth_percentage = Column(DECIMAL(5,2))

    is_twelfth_passed = Column(Boolean, default=False)
    college_name = Column(String(255))
    twelfth_pass_year = Column(Integer)
    twelfth_percentage = Column(DECIMAL(5,2))

    is_diploma_student = Column(Boolean, default=False)

    family_income = Column(DECIMAL(12,2), nullable=False)
    family_members_count = Column(Integer)

    family_farmer = Column(Boolean, default=False)
    family_covid_victim = Column(Boolean, default=False)
    family_military = Column(Boolean, default=False)
