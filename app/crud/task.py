from sqlalchemy.orm import Session
from app.models.task import Task
from app.schemas.task import TaskCreate, TaskUpdate

def create_task(db: Session, project_id: int, task_in: TaskCreate, owner_id: int):
    db_task = Task(
        title=task_in.title,
        description=task_in.description,
        project_id=project_id,
        owner_id=owner_id
    )
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task


def get_tasks(db: Session, project_id: int):
    return db.query(Task).filter(Task.project_id == project_id).all()

def get_task(db: Session, task_id: int):
    return db.query(Task).filter(Task.id == task_id).first()

def update_task(db: Session, task_id: int, task_in: TaskUpdate):
    task = get_task(db, task_id)
    if task:
        for key, value in task_in.dict(exclude_unset=True).items():
            setattr(task, key, value)
        db.commit()
        db.refresh(task)
    return task

def delete_task(db: Session, task_id: int):
    task = get_task(db, task_id)
    if task:
        db.delete(task)
        db.commit()
    return task

def assign_task_to_user(db: Session, task_id: int, user_id: int):
    task = get_task(db, task_id)
    if task:
        task.assignee_id = user_id
        db.commit()
        db.refresh(task)
    return task
