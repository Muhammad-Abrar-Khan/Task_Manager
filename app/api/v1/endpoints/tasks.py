from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, models, schemas
from app.schemas.task import Task, TaskBase, TaskCreate
from app.models.user import User
from app.api import deps

router = APIRouter()

@router.post("/", response_model=Task)
def create_task(
    *,
    db: Session = Depends(deps.get_db),
    task_in: TaskCreate,
    current_user: User = Depends(deps.get_current_user)
):
    task = crud.task.create_with_owner(db=db, obj_in=task_in, owner_id=current_user.id)
    return task

@router.get("/{id}", response_model=Task)
def read_task(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: User = Depends(deps.get_current_user)
):
    task = crud.task.get(db=db, id=id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task
