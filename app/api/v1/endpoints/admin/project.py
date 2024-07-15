from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api.deps import get_current_user, get_db
from app.schemas.project import Project,ProjectBase,ProjectCreate,ProjectInDB,ProjectInDBBase,ProjectUpdate
from app.models.user import User
from app.crud.project import get_project,get_projects,create_project, create_with_owner

router = APIRouter()

@router.get("/admin/project", response_model=List[Project])
def list_all_projects(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    if not current_user.is_superuser:
        raise HTTPException(status_code=403, detail="Not authorized")
    return get_projects(db=db)

@router.post("/admin/project", response_model=Project)
def create_project(
    project_in: ProjectCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    if not current_user.is_superuser:
        raise HTTPException(status_code=403, detail="Not authorized")
    return create_project(db=db, project_in=project_in)

@router.put("/admin/project/{project}", response_model=Project)
def update_project(
    project_id: int,
    project_in: ProjectUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    if not current_user.is_superuser:
        raise HTTPException(status_code=403, detail="Not authorized")
    return update_project(db=db, project_id=project_id, project_in=project_in)

@router.delete("/admin/project/{project}", response_model=Project)
def delete_project(
    project_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    if not current_user.is_superuser:
        raise HTTPException(status_code=403, detail="Not authorized")
    return delete_project(db=db, project_id=project_id)

@router.post("/admin/project/{project}/assign", response_model=Project)
def assign_project_to_user(
    project_id: int,
    user_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    if not current_user.is_superuser:
        raise HTTPException(status_code=403, detail="Not authorized")
    return assign_project_to_user(db=db, project_id=project_id, user_id=user_id)
