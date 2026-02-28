from sqlalchemy import Column, BigInteger, String, ForeignKey, DateTime
from sqlalchemy.sql import func
from app.database import Base

class SavedScholarship(Base):
    __tablename__ = "saved_scholarships"

    id = Column(BigInteger, primary_key=True, index=True)
    user_id = Column(String(36), ForeignKey("users.id"))
    scholarship_id = Column(BigInteger, ForeignKey("scholarships.scholarship_id"))
    created_at = Column(DateTime(timezone=True), server_default=func.now())