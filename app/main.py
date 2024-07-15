from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware
from app.api.v1.api import api_router
from app.core.config import Settings
from app.db.base import Base 
import os
from dotenv import load_dotenv

load_dotenv() 


settings = Settings()

app = FastAPI(title=settings.PROJECT_NAME)

app.add_middleware(DBSessionMiddleware, db_url=os.environ["DATABASE_URL"])


app.include_router(api_router, prefix=settings.API_V1_STR)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)


