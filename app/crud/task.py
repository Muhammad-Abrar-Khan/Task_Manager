from sqlalchemy.orm import Session
from app.models.task import Task
from app.schemas.task import TaskCreate

def get_tasks(db: Session, project_id: int):
    return db.query(Task).filter(Task.project_id == project_id).all()

def get_task(db: Session, task_id: int):
    return db.query(Task).filter(Task.id == task_id).first()

def create_task(db: Session, task: TaskCreate):
    db_task = Task(
        title=task.title, 
        description=task.description, 
        project_id=task.project_id, 
        parent_id=task.parent_id
    )
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def create_with_owner(db: Session, obj_in: TaskCreate, owner_id: int):
    db_task = Task(
        title=obj_in.title, 
        description=obj_in.description, 
        project_id=obj_in.project_id, 
        parent_id=obj_in.parent_id, 
        owner_id=owner_id
    )
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task
