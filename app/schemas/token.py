from pydantic import BaseModel
from typing import List

class Token(BaseModel):
    access_token: str
    token_type: str
    username: str
    scopes: List[str] = []

class Login(BaseModel):
    email: str
    password: str