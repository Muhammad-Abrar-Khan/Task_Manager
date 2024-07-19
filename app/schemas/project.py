from pydantic import BaseModel
from typing import Optional

class ProjectBase(BaseModel):
    title: str
    description: Optional[str] = None

class ProjectCreate(ProjectBase):
    pass

class ProjectUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None

class ProjectInDBBase(ProjectBase):
    id: int

    class Config:
        orm_mode = True

class Project(ProjectInDBBase):
    owner_id: Optional[int]

    class Config:
        orm_mode = True

class ProjectInDB(ProjectInDBBase):
    pass
