from sqlalchemy.orm import Session
from app.models.profile import Profile
from app.schemas.profile import ProfileCreate, ProfileUpdate

def get_profile(db: Session, profile_id: int):
    return db.query(Profile).filter(Profile.id == profile_id).first()

def create_profile(db: Session, profile_in: ProfileCreate):
    db_profile = Profile(**profile_in.dict())
    db.add(db_profile)
    db.commit()
    db.refresh(db_profile)
    return db_profile

def update_profile(db: Session, profile: Profile, profile_in: ProfileUpdate):
    for field, value in profile_in.dict().items():
        setattr(profile, field, value)
    db.commit()
    db.refresh(profile)
    return profile

def delete_profile(db: Session, profile: Profile):
    db.delete(profile)
    db.commit()
    return profile
