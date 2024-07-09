from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, models, schemas
from app.api import deps

router = APIRouter()

@router.post("/", response_model=schemas.Project)
def create_project(
    *,
    db: Session = Depends(deps.get_db),
    project_in: schemas.ProjectCreate,
    current_user: models.User = Depends(deps.get_current_user)
):
    project = crud.project.create_with_owner(db=db, obj_in=project_in, owner_id=current_user.id)
    return project

@router.get("/{id}", response_model=schemas.Project)
def read_project(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: models.User = Depends(deps.get_current_user)
):
    project = crud.project.get(db=db, id=id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return project
