from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app import crud, models, schemas
from app.api import deps

router = APIRouter()

@router.post("/", response_model=schemas.Project)
def create_project(
    *,
    db: Session = Depends(deps.get_db),
    project_in: schemas.ProjectCreate,
    current_user: models.user.User = Depends(deps.get_current_user)  
):
    project = crud.project.create_with_owner(db=db, obj_in=project_in, owner_id=current_user.id)
    return project

@router.get("/", response_model=List[schemas.Project])
def list_projects(
    db: Session = Depends(deps.get_db),
    current_user: models.user.User = Depends(deps.get_current_user)  
):
    return crud.project.get_projects(db=db)

@router.get("/{project_id}", response_model=schemas.Project)
def read_project(
    project_id: int,
    db: Session = Depends(deps.get_db),
    current_user: models.user.User = Depends(deps.get_current_user)  
):
    project = crud.project.get_project(db=db, project_id=project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    # Check if the user is assigned to the project (optional logic)
    if current_user not in project.users:
        raise HTTPException(status_code=403, detail="User not assigned to this project")
    return project

@router.put("/{project_id}", response_model=schemas.Project)
def update_project(
    project_id: int,
    project_in: schemas.ProjectUpdate,
    db: Session = Depends(deps.get_db),
    current_user: models.user.User = Depends(deps.get_current_user)  
):
    project = crud.project.get_project(db=db, project_id=project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    # Additional logic to check if user has permission to update (if needed)
    return crud.project.update_project(db=db, project_id=project_id, project_in=project_in)

@router.delete("/{project_id}", response_model=schemas.Project)
def delete_project(
    project_id: int,
    db: Session = Depends(deps.get_db),
    current_user: models.user.User = Depends(deps.get_current_user)  
):
    project = crud.project.get_project(db=db, project_id=project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    # Additional logic to check if user has permission to delete (if needed)
    return crud.project.delete_project(db=db, project_id=project_id)
