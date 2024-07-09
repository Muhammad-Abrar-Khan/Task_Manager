from datetime import datetime, timedelta
from typing import Any, Union
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from passlib.context import CryptContext
from app.core.config import settings

# Define a context for password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Define the OAuth2 password bearer scheme
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

ALGORITHM = "HS256"

# Function to verify a password against its hash
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

# Function to hash a password
def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

# Function to create access tokens
def create_access_token(subject: Union[str, Any], expires_delta: timedelta = None) -> str:
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode = {"exp": expire, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# Function to decode access tokens (Optional, if needed for your application)
def decode_access_token(token: str) -> dict:
    payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[ALGORITHM])
    return payload
