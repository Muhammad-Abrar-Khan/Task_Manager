from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app import crud, models, schemas
from app.api.deps import get_session
from app.core.utils import get_current_user
from app.models.user import User  # Ensure this path matches your project structure

router = APIRouter()

@router.post("/project/{project}/task", response_model=schemas.Task)
def create_task(
    task_in: schemas.TaskCreate,
    db: Session = Depends(get_session),
    current_user: User = Depends(get_current_user),
):
    return crud.task.create_task(db=db, task_in=task_in)


@router.get("/project/{project}/task", response_model=List[schemas.Task])
def list_tasks(
    db: Session = Depends(get_session),
    current_user: User = Depends(get_current_user),
):
    return crud.task.get_tasks(db=db)

@router.get("/project/{project}/task/{task}", response_model=schemas.Task)
def read_task(
    task_id: int,
    db: Session = Depends(get_session),
    current_user: User = Depends(get_current_user),
):
    task = crud.task.get_task(db=db, task_id=task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    # Additional logic to check if user has access to task (if needed)
    return task

@router.put("/project/{project}/task/{task}", response_model=schemas.Task)
def update_task(
    task_id: int,
    task_in: schemas.TaskUpdate,
    db: Session = Depends(get_session),
    current_user: User = Depends(get_current_user),
):
    task = crud.task.get_task(db=db, task_id=task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    # Additional logic to check if user has permission to update (if needed)
    return crud.task.update_task(db=db, task_id=task_id, task_in=task_in)

@router.delete("/project/{project}/task/{task}", response_model=schemas.Task)
def delete_task(
    task_id: int,
    db: Session = Depends(get_session),
    current_user: User = Depends(get_current_user),
):
    task = crud.task.get_task(db=db, task_id=task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    # Additional logic to check if user has permission to delete (if needed)
    return crud.task.delete_task(db=db, task_id=task_id)

@router.post("/project/{project}/task/{task}/assign", response_model=schemas.Task)
def assign_task_to_user(
    task_id: int,
    user_id: int,
    db: Session = Depends(get_session),
    current_user: User = Depends(get_current_user),
):
    task = crud.task.get_task(db=db, task_id=task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    # Additional logic to check if user has permission to assign task (if needed)
    return crud.task.assign_task_to_user(db=db, task_id=task_id, user_id=user_id)
