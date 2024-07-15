from fastapi import APIRouter
from app.api.v1.endpoints import login, users, projects, tasks, comments, profile
from app.api.v1.endpoints.admin import project, user

api_router = APIRouter()
api_router.include_router(project.router, tags=["project"])
api_router.include_router(user.router, tags=["user"])
api_router.include_router(profile.router,tags=["profiles"])
api_router.include_router(login.router, tags=["login"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(projects.router, tags=["projects"])
api_router.include_router(tasks.router, prefix="/tasks", tags=["tasks"])
api_router.include_router(comments.router, prefix="/comments", tags=["comments"])
