from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.comment import Comment as CommentSchema, CommentCreate
from app.crud.comment import create_with_owner, get_comment
from app.models.user import User
from app.api import deps

router = APIRouter()

@router.post("/", response_model=CommentSchema)
def create_comment(
    *,
    db: Session = Depends(deps.get_db),
    comment_in: CommentCreate,
    current_user: User = Depends(deps.get_current_user)
):
    comment = create_with_owner(db=db, obj_in=comment_in, owner_id=current_user.id)
    return comment

@router.get("/{id}", response_model=CommentSchema)
def read_comment(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: User = Depends(deps.get_current_user)
):
    comment = get_comment(db=db, id=id)
    if not comment:
        raise HTTPException(status_code=404, detail="Comment not found")
    return comment
