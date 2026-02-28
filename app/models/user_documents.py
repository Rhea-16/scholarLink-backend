
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

metadata = MetaData()
uploaded_via_enum = Enum(
    "manual_upload",
    "digilocker",
    "admin_upload",
    name="uploaded_via_enum"
)

verification_status_enum = Enum(
    "pending",
    "verified",
    "rejected",
    name="verification_status_enum"
)

user_documents = Table(
    "user_documents",
    metadata,

    Column("user_document_id", BigInteger, primary_key=True, autoincrement=True),

    Column("user_id", String(36),
           ForeignKey("users.user_id", ondelete="CASCADE"),
           nullable=False),

    Column("document_id", BigInteger,
           ForeignKey("master_documents.document_id", ondelete="CASCADE"),
           nullable=False),

    Column("file_url", String(500), nullable=False),
    Column("file_name", String(255)),
    Column("file_type", String(50)),

    Column("uploaded_via", uploaded_via_enum),
    Column("verification_status", verification_status_enum),

    Column("rejection_reason", Text),
    Column("version_number", Integer, default=1),
    Column("is_active", Boolean, default=True),

    Column("created_at", DateTime, server_default=func.now()),
)


Index("idx_user_id", user_documents.c.user_id)
Index("idx_verification_status", user_documents.c.verification_status)


