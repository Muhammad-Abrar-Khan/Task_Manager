from sqlalchemy.orm import Session
from app.models.project import Project
from app.schemas.project import ProjectCreate

def get_projects(db: Session):
    return db.query(Project).all()

def get_project(db: Session, project_id: int):
    return db.query(Project).filter(Project.id == project_id).first()

def create_project(db: Session, project: ProjectCreate):
    db_project = Project(name=project.name)
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project

def create_with_owner(db: Session, obj_in: ProjectCreate, owner_id: int):
    db_project = Project(name=obj_in.name, owner_id=owner_id)
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project
