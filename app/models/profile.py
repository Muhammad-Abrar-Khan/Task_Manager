from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base_class import Base

class Profile(Base):
    __tablename__ = "profiles"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False) 
    bio = Column(String, nullable=True, index=True)
    picture = Column(String, nullable=True, index=True)
    user = relationship("User", back_populates="profile")
