from pydantic_settings import BaseSettings

print("Config module is being imported")  # Add this line for debugging

class Settings(BaseSettings):
    ALGORITHM: str = "HS256"
    SECRET_KEY: str = "48a32608b94a00425a1af4fddebebd42942cb55aa40f7c5592c772b2c86bf6eb"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    SQLALCHEMY_DATABASE_URI: str = "postgresql://postgres:mak110@localhost:5432/task_manager"

    class Config:
        env_file = ".env"

settings = Settings()
