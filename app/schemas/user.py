# from pydantic import BaseModel, EmailStr
# from typing import Optional
# from datetime import datetime

# class UserBase(BaseModel):
#     email: EmailStr
#     is_active: Optional[bool] = True
#     is_superuser: Optional[bool] = False

# class UserCreate(UserBase):
#     name:str
#     password: str

# class UserUpdate(BaseModel):
#     email: Optional[EmailStr] = None
#     full_name: Optional[str] = None
#     is_active: Optional[bool] = None
#     is_superuser: Optional[bool] = None

# class User(UserBase):
#     id: int
#     created_at: datetime
#     updated_at: datetime

#     class Config:
#         orm_mode = True  # Pydantic v1 compatibility setting for SQLAlchemy models

from pydantic import BaseModel, EmailStr
import datetime
from typing import Optional


class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False

class UserUpdate(BaseModel):
    email: Optional[EmailStr] = None
    full_name: Optional[str] = None
    is_active: Optional[bool] = None
    is_superuser: Optional[bool] = None

class UserResponse(BaseModel):
    id: int
    username: str
    email: str

    class Config:
        orm_mode = True

class TokenSchema(BaseModel):
    access_token: str
    refresh_token: str

class TokenCreate(BaseModel):
    user_id: int
    access_token: str
    refresh_token: str
    status: bool
    created_date: datetime.datetime

class RequestDetails(BaseModel):
    email: str
    password: str

class ChangePassword(BaseModel):
    email: str
    old_password: str
    new_password: str
