from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from app.db.base_class import Base
from sqlalchemy.orm import relationship

class Comment(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True, index=True)
    parent_id = Column(Integer, ForeignKey('comments.id'), nullable=True)
    task_id = Column(Integer, ForeignKey('tasks.id'))
    content = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    parent = relationship("Comment", remote_side=[id], backref="replies", cascade="all, delete")
    task = relationship("Task", back_populates="comments")
    author_id = Column(Integer, ForeignKey("users.id"))  
    author = relationship("User", back_populates="comments")  

