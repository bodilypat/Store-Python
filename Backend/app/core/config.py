#app/core/config.py
from pydantic import BaseSettings
from pydantic import Field
from typing import Optional, List
from functools import lru_cache

class Settings(BaseSettings):
    #---------------------
    # Project Info
    #---------------------
    PROJECT_NAME: str = "POS Backend"
    PROJECT_VERSION: str = "1.0.0"
    API_PREFIX: str = "/api"
    DEBUG: bool = True

    #---------------------
    # Security
    #---------------------
    SECRET_KEY: str = Field(..., env="SECRET_KEY")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7  # 7 days
    ALGORITHM: str = "HS256"

    #---------------------
    # Database(PostgreSQL)
    #---------------------
    DB_HOST: str = "localhost"
    DB_PORT: int = 5432
    DB_USER: str = "postgres"
    DB_PASSWORD: str = "postgres"
    DB_NAME: str = "pos_db"
    DATABASE_URL: Optional[str] = None

    #---------------------
    # CORS
    #---------------------
    BACKEND_CORS_ORIGINS: List[str] = ["*"]

    #---------------------
    # Email (Optional Provider)
    #---------------------
    SMT_HOST: Optional[str] = None
    SMT_PORT: Optional[int] = None
    SMT_USER: Optional[str] = None
    SMT_PASSWORD: Optional[str] = None

    #---------------------
    # Computed Database URL
    #---------------------
    @property
    def database_url(self) -> str:
        if self.DATABASE_URL:
            return self.DATABASE_URL
        return( 
            f"postgresql+psycopg2://{self.DB_USER}:"
            f"{self.DB_PASSWORD}@{self.DB_HOST}:"
            f"{self.DB_PORT}/{self.DB_NAME}"
         )
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

# Singleton pattern for settings
@lru_cache()
def get_settings() -> Settings:
    return Settings()

settings = get_settings()



