from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.schemas.comment import Comment as CommentSchema, CommentCreate, CommentUpdate
from app.crud.comment import create_with_owner, get_comment, get_comments, update_comment, delete_comment
from app.models.user import User
from app.api import deps

router = APIRouter()

@router.get("/project/{project}/task/{task}/comment", response_model=List[CommentSchema])
def list_comments(
    *,
    db: Session = Depends(deps.get_db),
    project_id: int,
    task_id: int,
    current_user: User = Depends(deps.get_current_user)
):
    comments = get_comments(db=db, task_id=task_id)
    return comments

@router.post("/project/{project}/task/{task}/comment", response_model=CommentSchema)
def create_comment(
    *,
    db: Session = Depends(deps.get_db),
    project_id: int,
    task_id: int,
    comment_in: CommentCreate,
    current_user: User = Depends(deps.get_current_user)
):
    comment = create_with_owner(db=db, obj_in=comment_in, owner_id=current_user.id)
    return comment

@router.put("/project/{project}/task/{task}/comment/{comment}", response_model=CommentSchema)
def update_comment(
    *,
    db: Session = Depends(deps.get_db),
    project_id: int,
    task_id: int,
    comment_id: int,
    comment_in: CommentUpdate,
    current_user: User = Depends(deps.get_current_user)
):
    comment = get_comment(db=db, comment_id=comment_id)
    if not comment:
        raise HTTPException(status_code=404, detail="Comment not found")
    comment = update_comment(db=db, db_obj=comment, obj_in=comment_in)
    return comment

@router.delete("/project/{project}/task/{task}/comment/{comment}", response_model=CommentSchema)
def delete_comment(
    *,
    db: Session = Depends(deps.get_db),
    project_id: int,
    task_id: int,
    comment_id: int,
    current_user: User = Depends(deps.get_current_user)
):
    comment = get_comment(db=db, comment_id=comment_id)
    if not comment:
        raise HTTPException(status_code=404, detail="Comment not found")
    comment = delete_comment(db=db, comment_id=comment_id)
    return comment
