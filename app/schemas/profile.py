from pydantic import BaseModel

class ProfileBase(BaseModel):
    bio: str
    website: str

class ProfileCreate(ProfileBase):
    pass

class ProfileUpdate(ProfileBase):
    pass

class Profile(ProfileBase):
    id: int
    class Config:
        orm_mode = True
