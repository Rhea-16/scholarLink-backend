from sqlalchemy import Column, BigInteger, String, Text, Enum, Date, Numeric, Integer, Boolean, DateTime, func
from app.database import Base
from sqlalchemy.orm import relationship

class Scholarships(Base):
    __tablename__ = "scholarships"

    scholarship_id = Column(BigInteger, primary_key=True, index=True)
    scholarship_name = Column(String(255), nullable=False)
    provider_name = Column(String(255), nullable=False)
    provider_type = Column(Enum("government","private","ngo","trust","institute"),nullable=False)
    
    description = Column(Text,nullable=False)
    benefit_type = Column(Enum("tuition_fee","stipend","full_support","partial_support","one_time_grant","food service","room allowance"),nullable=False)
    benefit_amount = Column(Numeric(12,2))
    
    renewable = Column(Boolean, default=False)
    duration_years = Column(Integer)
    
    application_start_date = Column(Date,nullable = False)
    application_end_date = Column(Date,nullable = False)
    application_url = Column(String(500))
    
    status = Column(Enum("upcoming","active","closed","inactive"))
    is_featured = Column(Boolean, default=False)
    priority_score = Column(Integer, default=0)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )

    eligibility = relationship(
    "ScholarshipEligibility",
    back_populates="scholarship",
    uselist=True
    )