from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List

class CommentBase(BaseModel):
    content: str

class CommentCreate(CommentBase):
    task_id: int
    parent_id: Optional[int] = None

class Comment(CommentBase):
    id: int
    parent_id: Optional[int] = None
    task_id: int
    created_at: datetime

    class Config:
        orm_mode = True
