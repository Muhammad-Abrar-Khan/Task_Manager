from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.api.deps import get_session
from app.core.utils import get_current_user
from app.schemas.user import UserResponse, UserCreate, UserUpdate
from app.models.user import User
from app.crud.user import get_user, get_user_by_email, create_user, get_users, delete_user, update_user

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
def create_admin_user(
    user: UserCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_session)
):
    if not current_user.is_superuser:  # Ensure this matches your actual attribute name
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Only superadmins can create users")

    existing_user = db.query(User).filter_by(email=user.email).first()
    if existing_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")

    new_user = create_user(db=db, user=user)

    return UserResponse(id=new_user.id, username=new_user.username, email=new_user.email)

@router.put("/admin/user/{user_id}", response_model=UserResponse)
def update_admin_user(
    user_id: int,
    user_update: UserUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_session)
):
    if not current_user.is_superuser:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized")
    
    db_user = get_user(db=db, user_id=user_id)
    if not db_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    
    updated_user = update_user(db=db, user_id=user_id, user_update=user_update)
    
    return updated_user

@router.delete("/admin/user/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(
    user_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_session)
):
    if not current_user.is_superuser:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Only superadmins can delete users")

    user_to_delete = db.query(User).filter(User.id == user_id).first()
    if not user_to_delete:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    db.delete(user_to_delete)
    db.commit()

    return {"detail": "User deleted successfully"}
