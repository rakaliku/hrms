import os
from pydantic_settings  import BaseSettings

class Settings(BaseSettings):
    DB_USERNAME: str = "root"
    DB_PASSWORD: str = "Mysql%400195"
    # DB_PASSWORD: str = "Mysql@0195"
    DB_HOST: str = "127.0.0.1"
    DB_PORT: int = 3306
    DB_NAME: str = "hrms_db"

    class Config:
        env_file = ".env"  # You can use a .env file for sensitive data like passwords

settings = Settings()
