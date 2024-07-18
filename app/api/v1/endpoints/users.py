from fastapi import APIRouter, Depends, HTTPException, status
from app.schemas.user import UserResponse
from app.models.user import User as modelUser

from app.core.utils import get_current_user


router = APIRouter()

@router.get("/profile", response_model=UserResponse)
def get_profile(current_user: modelUser = Depends(get_current_user)):
    return current_user
