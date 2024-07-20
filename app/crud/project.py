from sqlalchemy.orm import Session, joinedload
from app.models.project import Project
from app.schemas.project import ProjectCreate, ProjectUpdate

def get_projects(db: Session):
    return db.query(Project).all()

def get_project(db: Session, project_id: int):
    return db.query(Project).filter(Project.id == project_id).first()

def create_project(db: Session, project: ProjectCreate):
    db_project = Project(title=project.title, description=project.description)
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project

def create_with_owner(db: Session, obj_in: ProjectCreate, owner_id: int):
    db_project = Project(title=obj_in.title, description=obj_in.description, owner_id=owner_id)
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project

def update_project(db: Session, project: Project, project_update: ProjectUpdate):
    for key, value in project_update.dict().items():
        setattr(project, key, value)
    db.commit()
    db.refresh(project)
    return project

def delete_project(db: Session, project_id: int):
    db_project = db.query(Project).filter(Project.id == project_id).first()
    if db_project:
        db.delete(db_project)
        db.commit()
        return db_project
    return None

def assign_project_to_user(db: Session, project_id: int, user_id: int):
    project = db.query(Project).filter(Project.id == project_id).first()
    if project:
        project.owner_id = user_id
        db.commit()
        db.refresh(project)
    return project
