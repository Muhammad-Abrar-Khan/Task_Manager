from pydantic import BaseModel
from typing import Optional

class ProfileBase(BaseModel):
    bio: Optional[str] = None
    picture: Optional[str] = None

class ProfileCreate(ProfileBase):
    pass

class ProfileUpdate(ProfileBase):
    pass

class Profile(ProfileBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True
