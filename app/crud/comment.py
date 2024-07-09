from sqlalchemy.orm import Session
from app.models.comment import Comment
from app.schemas.comment import CommentCreate

def get_comments(db: Session, task_id: int):
    return db.query(Comment).filter(Comment.task_id == task_id).all()

def get_comment(db: Session, comment_id: int):
    return db.query(Comment).filter(Comment.id == comment_id).first()

def create_comment(db: Session, comment: CommentCreate):
    db_comment = Comment(content=comment.content, task_id=comment.task_id, parent_id=comment.parent_id)
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment