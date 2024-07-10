from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, models, schemas
from app.schemas.project import ProjectBase, ProjectCreate, Project
from app.crud.project import get_project, get_projects, create_project, create_with_owner
from app.api import deps
from app.models.user import User

router = APIRouter()

@router.post("/", response_model=Project)
def create_project(
    *,
    db: Session = Depends(deps.get_db),
    project_in: ProjectCreate,
    current_user: User = Depends(deps.get_current_user)
):
    project = create_with_owner(db=db, obj_in=project_in, owner_id=current_user.id)
    return project

@router.get("/{id}", response_model=Project)
def read_project(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: User = Depends(deps.get_current_user)
):
    project = get_project(db=db, id=id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return project
