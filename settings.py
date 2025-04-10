import os


class Settings:
    PROJECT_NAME = "Facility Feed Service"
    BASE_DIR: str = os.path.dirname(os.path.abspath(__file__))
    DB_CONFIG = {
        "database": "feed_service",
        "host": "localhost",
        "user": "postgres",
        "password": "test",
        "port": 5432
    }

    class Config:
        case_sensitive = True
