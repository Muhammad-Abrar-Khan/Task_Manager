from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from app.db.base_class import Base

class Project(Base):
   __tablename__ = "projects"


   id = Column(Integer, primary_key=True, index=True)
   name = Column(String, index=True)
   created_at = Column(DateTime(timezone=True), server_default=func.now())
