from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api.deps import get_session
from app.core.utils import get_current_user
from app.schemas.user import UserResponse, UserCreate, UserUpdate
from app.models.user import User
from app.crud.user import get_user, get_user_by_email,create_user,get_users,delete_user,update_user

router = APIRouter()

@router.get("/admin/user", response_model=List[UserResponse])
def list_all_users(
    db: Session = Depends(get_session),
    current_user: User = Depends(get_current_user),
):
    if not current_user.is_superuser:
        raise HTTPException(status_code=403, detail="Not authorized")
    return get_users(db=db)

@router.post("/admin/user", response_model=UserResponse)
def create_user(
    user_in: UserCreate,
    db: Session = Depends(get_session),
    current_user: User = Depends(get_current_user),
):
    if not current_user.is_superuser:
        raise HTTPException(status_code=403, detail="Not authorized")
    return create_user(db=db, user_in=user_in)

@router.put("/admin/user/{user}", response_model=UserResponse)
def update_user(
    user_id: int,
    user_in: UserUpdate,
    db: Session = Depends(get_session),
    current_user: User = Depends(get_current_user),
):
    if not current_user.is_superuser:
        raise HTTPException(status_code=403, detail="Not authorized")
    return update_user(db=db, user_id=user_id, user_in=user_in)

@router.delete("/admin/user/{user}", response_model=UserResponse)
def delete_user(
    user_id: int,
    db: Session = Depends(get_session),
    current_user: User = Depends(get_current_user),
):
    if not current_user.is_superuser:
        raise HTTPException(status_code=403, detail="Not authorized")
    return delete_user(db=db, user_id=user_id)
