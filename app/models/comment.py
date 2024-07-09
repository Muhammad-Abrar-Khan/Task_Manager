
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.db.session import Base

class Comment(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True, index=True)
    parent_id = Column(Integer, ForeignKey('comments.id'), nullable=True)
    task_id = Column(Integer, ForeignKey('tasks.id'))
    content = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    parent = relationship("Comment", remote_side=[id], backref="replies")
    task = relationship("Task", back_populates="comments")