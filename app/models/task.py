
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.db.session import Base

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    parent_id = Column(Integer, ForeignKey('tasks.id'), nullable=True)
    project_id = Column(Integer, ForeignKey('projects.id'))
    title = Column(String, index=True)
    description = Column(String)
    status = Column(String, default="pending")
    assignee_id = Column(Integer, ForeignKey('users.id'), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    parent = relationship("Task", remote_side=[id], backref="subtasks")
    project = relationship("Project", back_populates="tasks")
    assignee = relationship("User", back_populates="tasks")
