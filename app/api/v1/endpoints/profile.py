from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api.deps import get_session
from app.core.utils import get_current_user
from app.models.user import User
from app.schemas.profile import Profile, ProfileBase, ProfileCreate, ProfileUpdate
from app.crud.profile import get_profile, create_profile, update_profile, get_profiles

router = APIRouter()

@router.get("/profile")
def read_profiles(
    db: Session = Depends(get_session),
    current_user: User = Depends(get_current_user),
):
    if not current_user.is_superuser:
        raise HTTPException(status_code=403, detail="Not authorized")
    return get_profiles(db)

@router.put("/profile")
def create_or_update_profile(
    profile_data: ProfileCreate,
    db: Session = Depends(get_session),
    current_user: User = Depends(get_current_user),
):
    db_profile = get_profile(db, current_user.id)
    if db_profile:
        return update_profile(db, db_profile, profile_data)
    else:
        return create_profile(db, profile_data, current_user.id)

@router.get("/users/profile")
def get_user_profile(
    db: Session = Depends(get_session),
    current_user: User = Depends(get_current_user),
):
    profile = get_profile(db, current_user.id)
    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found")
    return profile
