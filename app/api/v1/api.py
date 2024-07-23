from fastapi import APIRouter
from app.api.v1.endpoints import auth, projects, tasks, comments, profile,users
from app.api.v1.endpoints.admin import project, user

api_router = APIRouter()
api_router.include_router(project.router, tags=["project"])
api_router.include_router(user.router, tags=["user"])
api_router.include_router(profile.router,tags=["profiles"])
api_router.include_router(auth.router, tags=["auth"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(projects.router, tags=["projects"])
api_router.include_router(tasks.router, prefix="/tasks", tags=["tasks"])
api_router.include_router(comments.router, prefix="/comments", tags=["comments"])
