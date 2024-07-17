from fastapi import APIRouter, Depends, HTTPException, status
from app.schemas.user import UserResponse
from app.models.user import User as modelUser

from app.core.utils import get_current_user


router = APIRouter()

@router.get("/profile", response_model=UserResponse)
def get_profile(current_user: modelUser = Depends(get_current_user)):
    return current_user

# @router.post("/login", response_model=Token)  # Update response_model to Token
# def login(form_data: Login, db: Session = Depends(deps.get_db)):
#     user = crud.user.authenticate(db, email=form_data.email, password=form_data.password)
#     if not user:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Incorrect email or password",
#             headers={"WWW-Authenticate": "Bearer"},
#         )
#     access_token = crud.user.create_access_token(user.id)
#     return {"access_token": access_token, "token_type": "bearer"}

# @router.post("/register", response_model=User)
# def register(user_in: UserCreate, db: Session = Depends(deps.get_db)):
#     user = crud.user.create(db, obj_in=user_in)
#     return user