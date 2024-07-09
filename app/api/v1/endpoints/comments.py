from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, models, schemas
from app.schemas.comment import Comment, CommentBase, CommentCreate
from app.api import deps

router = APIRouter()

@router.post("/", response_model=Comment)
def create_comment(
    *,
    db: Session = Depends(deps.get_db),
    comment_in: CommentCreate,
    current_user: models.User = Depends(deps.get_current_user)
):
    comment = crud.comment.create_with_owner(db=db, obj_in=comment_in, owner_id=current_user.id)
    return comment

@router.get("/{id}", response_model=schemas.Comment)
def read_comment(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: models.User = Depends(deps.get_current_user)
):
    comment = crud.comment.get(db=db, id=id)
    if not comment:
        raise HTTPException(status_code=404, detail="Comment not found")
    return comment
