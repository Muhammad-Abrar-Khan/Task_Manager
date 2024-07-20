from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app import crud, models, schemas
from app.api.deps import get_session
from app.core.utils import get_current_user

router = APIRouter()

@router.get("/project", response_model=List[schemas.Project])
def list_projects(
    db: Session = Depends(get_session),
    current_user: models.user.User = Depends(get_current_user)  
):
    return crud.project.get_projects(db=db)

@router.get("/project/{project_id}", response_model=schemas.Project)
def read_project(
    project_id: int,
    db: Session = Depends(get_session),
    current_user: models.user.User = Depends(get_current_user)
):
    project = crud.project.get_project(db=db, project_id=project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return project
