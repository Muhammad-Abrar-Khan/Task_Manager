from sqlalchemy.orm import Session
from app.models.comment import Comment
from app.schemas.comment import CommentCreate, CommentUpdate

def get_comments_by_task(db: Session, task_id: int):
    return db.query(Comment).filter(Comment.task_id == task_id).all()

def create_comment(db: Session, comment: CommentCreate):
    db_comment = Comment(content=comment.content, task_id=comment.task_id, parent_id=comment.parent_id)
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment

def create_with_owner(db: Session, obj_in: CommentCreate, owner_id: int, task_id: int):
    parent_id = obj_in.parent_id if obj_in.parent_id and obj_in.parent_id > 0 else None
    db_comment = Comment(content=obj_in.content, task_id=task_id, parent_id=parent_id, author_id=owner_id)
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment

def get_comment(db: Session, comment_id: int):
    return db.query(Comment).filter(Comment.id == comment_id).first()

def update_comment_crud(db: Session, db_obj: Comment, obj_in: CommentUpdate):
    obj_data = obj_in.dict(exclude_unset=True)
    for field in obj_data:
        setattr(db_obj, field, obj_data[field])
    db.commit()
    db.refresh(db_obj)
    return db_obj


def delete_comment_crud(db: Session, db_obj: Comment):
    if db_obj.replies:
        for reply in db_obj.replies:
            db.delete(reply)
    db.delete(db_obj)
    db.commit()
    return db_obj


