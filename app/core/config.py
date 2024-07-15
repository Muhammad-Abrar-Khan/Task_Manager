from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Task Manager"
    API_V1_STR: str = "/api/v1"    
    ALGORITHM: str = "HS256"
    SECRET_KEY: str = "48a32608b94a00425a1af4fddebebd42942cb55aa40f7c5592c772b2c86bf6eb"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    database_url: str = "postgresql+psycopg2://postgres:postgres@db:5432/test_db"

    class Config:
        env_file = ".env"

settings = Settings()
