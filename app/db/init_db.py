from app.db.session import SessionLocal, engine, Base
from app.models import user, project, task, comment

def init_db():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    init_db()
