from sqlalchemy import (
    Column,
    BigInteger,
    String,
    Enum,
    Numeric,
    Integer,
    DateTime,
    ForeignKey,
    JSON,
    func
)
from sqlalchemy.orm import relationship
from app.database import Base


class ScholarshipEligibility(Base):
    __tablename__ = "scholarship_eligibility"

    eligibility_id = Column(BigInteger, primary_key=True, index=True)

    scholarship_id = Column(
        BigInteger,
        ForeignKey("scholarships.scholarship_id"),
        nullable=False
    )

    domicile_state = Column(String(50), nullable=True)

    nationality = Column(String(50), nullable=True, default="India")

    gender = Column(
        Enum("any", "male", "female", "other"),
        nullable=True,
        default="any"
    )

    category = Column(
        Enum(
            "general", "obc", "sc", "st",
            "nt", "sbc", "sebc",
            "ews", "ebc",
            "any", "orphanWithoutCaste"
        ),
        nullable=True,
        default="general"
    )

    family_income_max = Column(Numeric(12, 2), nullable=True)

    min_marks_percent = Column(Numeric(5, 2), nullable=True)

    education_level = Column(
        Enum("school", "diploma", "ug", "pg", "any"),
        nullable=True,
        default="any"
    )

    course_stream = Column(String(100), nullable=True)

    year_min = Column(Integer, nullable=True)

    year_max = Column(Integer, nullable=True)

    criteria_json = Column(JSON, nullable=True)

    # Timestamps
    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )

    # Relationship back to Scholarship
    scholarship = relationship(
        "Scholarships",
        back_populates="eligibility"
    )