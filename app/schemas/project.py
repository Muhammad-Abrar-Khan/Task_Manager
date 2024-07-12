from pydantic import BaseModel
from typing import Optional

class ProjectBase(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None

class ProjectCreate(ProjectBase):
    title: str

class ProjectUpdate(ProjectBase):
    pass

class ProjectInDBBase(ProjectBase):
    id: int
    title: str

    class Config:
        from_attributes = True

class Project(ProjectInDBBase):
    pass

class ProjectInDB(ProjectInDBBase):
    pass
