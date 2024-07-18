# from fastapi import APIRouter, Depends, HTTPException
# from fastapi.security import OAuth2PasswordRequestForm
# from sqlalchemy.orm import Session
# from app.schemas.user import UserCreate, User
# from app.schemas.token import Token, Login
# from app.crud.user import create_user, get_user_by_email
# from app.core.security import verify_password, create_access_token
# from app.api.deps import get_db

# router = APIRouter()

# @router.post("/register", response_model=User)
# def register_user(user: UserCreate, db: Session = Depends(get_db)):
#     db_user = get_user_by_email(db, email=user.email)
#     if db_user:
#         raise HTTPException(status_code=400, detail="Email already registered")
#     return create_user(db=db, user=user)

# @router.post("/login", response_model=Token)
# def login_user(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
#     user = db.query(User).filter(User.email == form_data.username).first()
#     if not user or not verify_password(form_data.password, user.hashed_password):
#         raise HTTPException(status_code=401, detail="Incorrect username or password")
#     access_token = create_access_token(data={"sub": user.email})
#     return {"access_token": access_token, "token_type": "bearer"}


# @router.post("/logout")
# def logout_user():
#     return {"msg": "Successfully logged out"}



from app.api.deps import get_session
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.user import RequestDetails, TokenSchema,UserCreate,UserResponse
from app.models.user import User, TokenTable
from app.core.utils import get_hashed_password, verify_password, create_access_token, create_refresh_token
from app.core.security import JWTBearer, decodeJWT
from app.crud.user import create_user

router = APIRouter()

@router.post("/register", response_model=UserResponse)
def register_user(user: UserCreate, db: Session = Depends(get_session)):
    existing_user = db.query(User).filter_by(email=user.email).first()
    if existing_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")

    new_user = create_user(db=db, user=user)

    return UserResponse(id=new_user.id, username=new_user.username, email=new_user.email)


@router.post('/login', response_model=TokenSchema)
def login(request: RequestDetails, db: Session = Depends(get_session)):
    user = db.query(User).filter(User.email == request.email).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Incorrect email or password")
    
    if not verify_password(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Incorrect email or password")
    
    access_token = create_access_token(user.id)
    refresh_token = create_refresh_token(user.id)

    token_db = TokenTable(user_id=user.id, access_token=access_token, refresh_token=refresh_token, status=True)
    db.add(token_db)
    db.commit()
    db.refresh(token_db)
    
    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
    }


@router.post('/logout')
def logout(token: str = Depends(JWTBearer()), db: Session = Depends(get_session)):
    payload = decodeJWT(token)
    if not payload:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid token or expired token")
    
    user_id = payload['sub']
    token_record = db.query(TokenTable).filter(TokenTable.user_id == user_id, TokenTable.access_token == token).first()
    if token_record:
        token_record.status = False
        db.commit()
        db.refresh(token_record)
        return {"message": "Logout successful"}
    
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Token not found")
