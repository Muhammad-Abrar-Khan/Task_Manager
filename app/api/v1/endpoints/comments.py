from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.api.deps import get_session
from app.core.utils import get_current_user
from app.models.comment import Comment
from app.models.project import Project
from app.models.task import Task
from app.schemas.comment import Comment as CommentSchema, CommentCreate, CommentUpdate
from app.crud.comment import create_with_owner, delete_comment_crud, get_comment, get_comments_by_task, update_comment_crud
from app.models.user import User

router = APIRouter()


@router.post("/project/{project}/task/{task}/comment", response_model=CommentSchema)
def create_comment(
    *,
    db: Session = Depends(get_session),
    project_id: int,
    task_id: int,
    comment_in: CommentCreate,
    current_user: User = Depends(get_current_user)
):
    # Check if the project exists
    if not db.query(Project).filter(Project.id == project_id).first():
        raise HTTPException(status_code=404, detail="Project not found")
    
    # Check if the task exists
    if not db.query(Task).filter(Task.id == task_id).first():
        raise HTTPException(status_code=404, detail="Task not found")
    
    if comment_in.parent_id:
        parent_comment = db.query(Comment).filter(Comment.id == comment_in.parent_id).first()
        if not parent_comment:
            raise HTTPException(status_code=404, detail="Parent comment not found")

    comment = create_with_owner(db=db, obj_in=comment_in, owner_id=current_user.id, task_id=task_id)
    return comment

@router.get("/project/{project}/task/{task}/comment", response_model=List[CommentSchema])
def list_comments(
    *,
    db: Session = Depends(get_session),
    project_id: int,
    task_id: int,
    current_user: User = Depends(get_current_user)
):
    # Check if the project exists
    if not db.query(Project).filter(Project.id == project_id).first():
        raise HTTPException(status_code=404, detail="Project not found")
    
    # Check if the task exists
    if not db.query(Task).filter(Task.id == task_id).first():
        raise HTTPException(status_code=404, detail="Task not found")

    comments = get_comments_by_task(db=db, task_id=task_id)
    return comments

@router.put("/project/{project}/task/{task}/comment/{comment_id}", response_model=CommentSchema)
def update_comment(
    *,
    db: Session = Depends(get_session),
    project_id: int,
    task_id: int,
    comment_id: int,
    comment_in: CommentUpdate,
    current_user: User = Depends(get_current_user)
):
    # Check if the project exists
    if not db.query(Project).filter(Project.id == project_id).first():
        raise HTTPException(status_code=404, detail="Project not found")

    # Check if the task exists
    if not db.query(Task).filter(Task.id == task_id).first():
        raise HTTPException(status_code=404, detail="Task not found")

    # Get the existing comment
    comment = get_comment(db=db, comment_id=comment_id)
    if not comment:
        raise HTTPException(status_code=404, detail="Comment not found")

    updated_comment = update_comment_crud(db=db, db_obj=comment, obj_in=comment_in)
    return updated_comment

@router.delete("/project/{project}/task/{task}/comment/{comment_id}", response_model=CommentSchema)
def delete_comment(
    *,
    db: Session = Depends(get_session),
    project_id: int,
    task_id: int,
    comment_id: int,
    current_user: User = Depends(get_current_user)
):
    # Check if the project exists
    if not db.query(Project).filter(Project.id == project_id).first():
        raise HTTPException(status_code=404, detail="Project not found")

    # Check if the task exists
    if not db.query(Task).filter(Task.id == task_id).first():
        raise HTTPException(status_code=404, detail="Task not found")

    # Get the existing comment
    comment = get_comment(db=db, comment_id=comment_id)
    if not comment:
        raise HTTPException(status_code=404, detail="Comment not found")

    deleted_comment = delete_comment_crud(db=db, db_obj=comment)
    return deleted_comment
