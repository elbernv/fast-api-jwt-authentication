import logging
import os
from functools import lru_cache
from typing import Any

from pydantic import BaseSettings

log = logging.getLogger("uvicorn")


class Settings(BaseSettings):
    environment: str = os.getenv("ENVIRONMENT", "dev")

    api_base_url: str = os.getenv("BASE_URL", "http://localhost:8000")

    redis_url: str = os.environ.get("REDIS_URL", "redis://localhost:6379")
    redis_password: str = os.getenv("REDIS_PASSWORD", "")
    redis_db: int = int(os.getenv("REDIS_DB", "0"))

    sqlite_url: str = os.environ.get("SQLITE_URL", "sqlite:///./users.db")

    jwt_secret: str = os.environ.get(
        "JWT_SECRET_KEY", "zCaud3gzRN9NoheRQv2J6SpBdbrkihmskwl5vfhOeK3LF"
    )
    jwt_algorithm: str = os.environ.get("JWT_ALGORITHM", "HS256")
    jwt_exp: int = int(os.environ.get("JWT_EXP", "30"))
