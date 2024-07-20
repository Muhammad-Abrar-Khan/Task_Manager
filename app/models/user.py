from datetime import datetime, timezone
from sqlalchemy import Boolean, Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from app.db.base_class import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True, nullable=True)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String(100), nullable=False)
    is_active = Column(Boolean(), default=True)
    is_superuser = Column(Boolean(), default=False)
    profile = relationship("Profile", back_populates="user", uselist=False)
    tasks = relationship("Task", back_populates="owner", primaryjoin="User.id == Task.owner_id")
    comments = relationship("Comment", back_populates="author")

class TokenTable(Base):
    __tablename__ = "token"
    user_id = Column(Integer, primary_key=True, index=True)
    access_token = Column(String(450), primary_key=True)
    refresh_token = Column(String(450), nullable=False)
    status = Column(Boolean, default=True)
    created_date = Column(DateTime, default=datetime.now(timezone.utc))

