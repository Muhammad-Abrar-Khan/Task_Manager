from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api.deps import get_session
from app.core.utils import get_current_user
from app.schemas.project import Project,ProjectBase,ProjectCreate,ProjectInDB,ProjectInDBBase,ProjectUpdate
from app.models.user import User
from app.crud.project import assign_project_to_user, get_project,get_projects,create_project, create_with_owner,update_project

router = APIRouter()

@router.get("/admin/project", response_model=List[Project])
def list_all_projects(
    db: Session = Depends(get_session),
    current_user: User = Depends(get_current_user),
):
    if not current_user.is_superuser:
        raise HTTPException(status_code=403, detail="Not authorized")
    return get_projects(db=db)

@router.post("/admin/project", response_model=Project)
def create_project(
    project_in: ProjectCreate,
    db: Session = Depends(get_session),
    current_user: User = Depends(get_current_user),
):
    if not current_user.is_superuser:
        raise HTTPException(status_code=403, detail="Not authorized")
    return create_with_owner(db=db, obj_in=project_in, owner_id=current_user.id)

@router.put("/admin/project/{project_id}", response_model=Project)
def update_project_details(
    project_id: int,
    project_update: ProjectUpdate,
    db: Session = Depends(get_session),
    current_user: User = Depends(get_current_user),
):
    if not current_user.is_superuser:
        raise HTTPException(status_code=403, detail="Not authorized")
    
    db_project = get_project(db=db, project_id=project_id)
    if db_project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    
    return update_project(db=db, project=db_project, project_update=project_update)

@router.delete("/admin/project/{project_id}", response_model=dict)
def delete_project(
    project_id: int,
    db: Session = Depends(get_session),
    current_user: User = Depends(get_current_user),
):
    if not current_user.is_superuser:
        raise HTTPException(status_code=403, detail="Not authorized")
    
    db_project = get_project(db=db, project_id=project_id)
    if db_project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    
    db.delete(db_project)
    db.commit()
    return {"message": "Project deleted successfully"}

@router.post("/admin/project/{project_id}/assign/{user_id}", response_model=Project)
def assign_project(
    project_id: int,
    user_id: int,
    db: Session = Depends(get_session),
    current_user: User = Depends(get_current_user),
):
    if not current_user.is_superuser:
        raise HTTPException(status_code=403, detail="Not authorized")

    assigned_project = assign_project_to_user(db=db, project_id=project_id, user_id=user_id)
    if assigned_project is None:
        raise HTTPException(status_code=404, detail="Project not found")

    return assigned_project