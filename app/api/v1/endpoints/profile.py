from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api.deps import get_current_user, get_db
from app.models.user import User
from app.schemas.profile import Profile, ProfileBase, ProfileCreate, ProfileUpdate
from app.crud.profile import get_profile, create_profile, delete_profile, update_profile

router = APIRouter()

@router.get("/", response_model=List[Profile])
def read_profiles(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return get_profile(db=db)

@router.post("/", response_model=Profile)
def create_profile(profile_in: ProfileCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return create_profile(db=db, profile_in=profile_in)

@router.put("/{profile_id}", response_model=Profile)
def update_profile(profile_id: int, profile_in: ProfileUpdate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    profile = get_profile(db=db, profile_id=profile_id)
    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found")
    return update_profile(db=db, profile=profile, profile_in=profile_in)

@router.delete("/{profile_id}", response_model=Profile)
def delete_profile(profile_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    profile = get_profile(db=db, profile_id=profile_id)
    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found")
    return delete_profile(db=db, profile=profile)
