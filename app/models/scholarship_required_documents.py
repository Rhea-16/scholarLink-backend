from sqlalchemy import (
    MetaData, Table, Column,
    BigInteger, String, Text,
    Boolean, Integer, DateTime,
    ForeignKey, Enum, Index
)
from sqlalchemy.dialects.mysql import JSON
from sqlalchemy.sql import func
from database import engine
import enum

from app.database import Base

metadata = MetaData()
# -------------------
# SCHOLARSHIP REQUIRED DOCUMENTS
# -------------------

scholarship_required_documents = Table(
    "scholarship_required_documents",
    metadata,

    Column("id", BigInteger, primary_key=True, autoincrement=True),
    Column("scholarship_id", BigInteger,
           ForeignKey("scholarships.scholarship_id", ondelete="CASCADE"),
           nullable=False),

    Column("document_id", BigInteger,
           ForeignKey("master_documents.document_id", ondelete="CASCADE"),
           nullable=False),

    Column("is_mandatory", Boolean, default=True),
    Column("is_condition_based", Boolean, default=False),
    Column("condition_json", JSON),
    Column("remarks", Text),
    Column("display_order", Integer, default=1),
    Column("created_at", DateTime, server_default=func.now()),
)
