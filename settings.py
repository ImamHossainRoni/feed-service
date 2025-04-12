import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    PROJECT_NAME = "Facility Feed Service"
    BASE_DIR: str = os.path.dirname(os.path.abspath(__file__))
    DB_CONFIG = {
        "database": os.getenv("DB_NAME", "feed_service"),
        "host": os.getenv("DB_HOST", "localhost"),
        "user": os.getenv("DB_USER", "postgres"),
        "password": os.getenv("DB_PASSWORD", "test"),
        "port": int(os.getenv("DB_PORT", 5432))
    }

    class Config:
        case_sensitive = True
