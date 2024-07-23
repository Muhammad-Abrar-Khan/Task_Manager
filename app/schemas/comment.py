from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class CommentBase(BaseModel):
    content: str
    parent_id: Optional[int] = None

class CommentCreate(CommentBase):
    pass


class CommentUpdate(BaseModel):
    content: Optional[str] = None

class Comment(CommentBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True 
