from sqlalchemy import Column, Integer, String, Boolean, Enum
from app.db.database import Base
import enum

class Role(str, enum.Enum):
    ADMIN = "admin"
    DOCTOR = "doctor"
    PATIENT = "patient"

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    first_name = Column(String, nullable=True)
    last_name = Column(String, nullable=True)
    role = Column(Enum(Role), default=Role.PATIENT, nullable=False)
    is_active = Column(Boolean, default=True)
