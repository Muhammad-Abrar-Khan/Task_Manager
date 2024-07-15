from sqlalchemy import Boolean, Column, Integer, String
from app.db.base_class import Base
from sqlalchemy.orm import relationship

class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean(), default=True)
    is_admin = Column(Boolean(), default=False)

    profile = relationship("Profile", back_populates="user", uselist=False)
