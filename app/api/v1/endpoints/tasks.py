from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app import crud, models, schemas
from app.api.deps import get_session
from app.core.utils import get_current_user
from app.models.user import User 

router = APIRouter()

# main router

@router.post("/project/{project_id}/task", response_model=schemas.Task)
def create_task(
    project_id: int,
    task_in: schemas.TaskCreate,
    db: Session = Depends(get_session),
    current_user: User = Depends(get_current_user),
):
    return crud.task.create_task(db=db, project_id=project_id, task_in=task_in, owner_id=current_user.id)


@router.get("/project/{project_id}/task", response_model=List[schemas.Task])
def list_tasks(
    project_id: int,
    db: Session = Depends(get_session),
    current_user: User = Depends(get_current_user),
):
    return crud.task.get_tasks(db=db, project_id=project_id)

@router.get("/project/{project_id}/task/{task_id}", response_model=schemas.Task)
def read_task(
    project_id: int,
    task_id: int,
    db: Session = Depends(get_session),
    current_user: User = Depends(get_current_user),
):
    task = crud.task.get_task(db=db, task_id=task_id)
    if not task or task.project_id != project_id:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.put("/project/{project_id}/task/{task_id}", response_model=schemas.Task)
def update_task(
    project_id: int,
    task_id: int,
    task_in: schemas.TaskUpdate,
    db: Session = Depends(get_session),
    current_user: User = Depends(get_current_user),
):
    task = crud.task.get_task(db=db, task_id=task_id)
    if not task or task.project_id != project_id:
        raise HTTPException(status_code=404, detail="Task not found")
    return crud.task.update_task(db=db, task_id=task_id, task_in=task_in)

@router.delete("/project/{project_id}/task/{task_id}", response_model=schemas.Task)
def delete_task(
    project_id: int,
    task_id: int,
    db: Session = Depends(get_session),
    current_user: User = Depends(get_current_user),
):
    task = crud.task.get_task(db=db, task_id=task_id)
    if not task or task.project_id != project_id:
        raise HTTPException(status_code=404, detail="Task not found")
    return crud.task.delete_task(db=db, task_id=task_id)

@router.post("/project/{project_id}/task/{task_id}/assign", response_model=schemas.Task)
def assign_task_to_user(
    project_id: int,
    task_id: int,
    user_id: int,
    db: Session = Depends(get_session),
    current_user: User = Depends(get_current_user),
):
    task = crud.task.get_task(db=db, task_id=task_id)
    if not task or task.project_id != project_id:
        raise HTTPException(status_code=404, detail="Task not found")
    return crud.task.assign_task_to_user(db=db, task_id=task_id, user_id=user_id)
