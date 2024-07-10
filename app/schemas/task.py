from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List

class TaskBase(BaseModel):
    title: str
    description: str

class TaskCreate(TaskBase):
    project_id: int
    parent_id: Optional[int] = None

class Task(TaskBase):
    id: int
    parent_id: Optional[int] = None
    project_id: int
    status: str
    owner_id: Optional[int] = None
    created_at: datetime

    class Config:
        orm_mode = True