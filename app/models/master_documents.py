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


# -------------------
# ENUMS
# -------------------

document_category_enum = Enum(
    "identity",
    "income",
    "academic",
    "residence",
    "category",
    "medical",
    "special_condition",
    "other",
    name="document_category_enum"
)

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


# -------------------
# MASTER DOCUMENTS
# -------------------

master_documents = Table(
    "master_documents",
    metadata,

    Column("document_id", BigInteger, primary_key=True, autoincrement=True),
    Column("document_code", String(100), unique=True, nullable=False),
    Column("document_name", String(255), nullable=False),
    Column("description", Text),
    Column("document_category", document_category_enum, nullable=False),
    Column("is_digilocker_supported", Boolean, default=False),
    Column("is_active", Boolean, default=True),
    Column("created_at", DateTime, server_default=func.now()),
    Column("updated_at", DateTime, server_default=func.now(), onupdate=func.now()),
)


