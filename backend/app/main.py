from fastapi import FastAPI

from app.api.v1.score import router as score_router

app = FastAPI(
    title="Decision Wheel API",
    version="0.1.0",
)

app.include_router(score_router, prefix="/api/v1")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/ready")
def ready() -> dict[str, str]:
    return {"status": "ready"}
