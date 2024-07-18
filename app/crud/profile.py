from sqlalchemy.orm import Session
from app.models.profile import Profile
from app.schemas.profile import ProfileCreate, ProfileUpdate

def get_profile(db: Session, user_id: int):
    return db.query(Profile).filter(Profile.user_id == user_id).first()

def get_profiles(db: Session):
    return db.query(Profile).all()

def create_profile(db: Session, profile: ProfileCreate, user_id: int):
    db_profile = Profile(**profile.dict(), user_id=user_id)
    db.add(db_profile)
    db.commit()
    db.refresh(db_profile)
    return db_profile

def update_profile(db: Session, db_profile: Profile, profile: ProfileUpdate):
    for key, value in profile.dict().items():
        setattr(db_profile, key, value)
    db.commit()
    db.refresh(db_profile)
    return db_profile
