# from fastapi import Depends, HTTPException, status
# from jose import JWTError, jwt
# from sqlalchemy.orm import Session
# from app.core.config import settings
# from app.models.user import User
# from app.schemas.token import Token
# from app.core.security import oauth2_scheme
# from app.db.session import SessionLocal
# from typing import Generator

# ALGORITHM = settings.ALGORITHM

# def get_db() -> Generator:
#     try:
#         db = SessionLocal()
#         yield db
#     finally:
#         db.close()

# def get_current_user(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)) -> User:
#     credentials_exception = HTTPException(
#         status_code=status.HTTP_401_UNAUTHORIZED,
#         detail="Could not validate credentials",
#         headers={"WWW-Authenticate": "Bearer"},
#     )
#     try:
#         payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[ALGORITHM])
#         user_id: str = payload.get("sub")
#         if user_id is None:
#             raise credentials_exception
#         token_data = Token(user_id=user_id)
#     except JWTError:
#         raise credentials_exception
#     user = db.query(User).filter(User.id == token_data.user_id).first()
#     if user is None:
#         raise credentials_exception
#     return user

# def get_current_active_user(current_user: User = Depends(get_current_user)) -> User:
#     if not current_user.is_active:
#         raise HTTPException(status_code=400, detail="Inactive user")
#     return current_user

# def get_current_active_admin(current_user: User = Depends(get_current_user)) -> User:
#     if not current_user.is_admin:
#         raise HTTPException(status_code=400, detail="The user doesn't have enough privileges")
#     return current_user

# import schemas
# import models
# from models import User
# from db.session import SessionLocal
# from fastapi import FastAPI, Depends, HTTPException,status
# from sqlalchemy.orm import Session

from app.db.session import SessionLocal


def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()