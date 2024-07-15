from fastapi import APIRouter
from app.api.v1.endpoints import login, users, projects, tasks, comments
from app.api.v1.endpoints import profile



api_router = APIRouter()
api_router.include_router(profile.router, prefix="/profiles", tags=["profiles"])
api_router.include_router(login.router, prefix="/login", tags=["login"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(projects.router, prefix="/projects", tags=["projects"])
api_router.include_router(tasks.router, prefix="/tasks", tags=["tasks"])
api_router.include_router(comments.router, prefix="/comments", tags=["comments"])
