from fastapi import FastAPI, HTTPException

from src.infrastructure.config import get_settings
from src.infrastructure.database.health import database_is_available

settings = get_settings()

app = FastAPI(title=settings.app_name, version=settings.app_version)


@app.get("/health", tags=["system"])
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/health/ready", tags=["system"])
def readiness() -> dict[str, str]:
    if not database_is_available():
        raise HTTPException(status_code=503, detail="Database is unavailable")

    return {"status": "ok", "database": "ok"}
