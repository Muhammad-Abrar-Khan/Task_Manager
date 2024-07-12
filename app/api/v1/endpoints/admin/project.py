from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api.deps import get_current_user, get_db
from app import crud, models, schemas

router = APIRouter()

@router.get("/admin/project", response_model=List[schemas.Project])
def list_all_projects(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user),
):
    if not current_user.is_superuser:
        raise HTTPException(status_code=403, detail="Not authorized")
    return crud.project.get_projects(db=db)

@router.put("/admin/project/{project_id}", response_model=schemas.Project)
def update_project(
    project_id: int,
    project_in: schemas.ProjectUpdate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user),
):
    if not current_user.is_superuser:
        raise HTTPException(status_code=403, detail="Not authorized")
    return crud.project.update_project(db=db, project_id=project_id, project_in=project_in)

@router.delete("/admin/project/{project_id}", response_model=schemas.Project)
def delete_project(
    project_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user),
):
    if not current_user.is_superuser:
        raise HTTPException(status_code=403, detail="Not authorized")
    return crud.project.delete_project(db=db, project_id=project_id)

@router.post("/admin/project/{project_id}/assign", response_model=schemas.Project)
def assign_project_to_user(
    project_id: int,
    user_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user),
):
    if not current_user.is_superuser:
        raise HTTPException(status_code=403, detail="Not authorized")
    return crud.project.assign_project_to_user(db=db, project_id=project_id, user_id=user_id)
