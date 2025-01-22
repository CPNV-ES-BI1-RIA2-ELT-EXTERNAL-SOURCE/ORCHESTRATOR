from fastapi import APIRouter

from app.routes import pipelines

api_router = APIRouter()

api_router.include_router(pipelines.router, prefix="/pipeline", tags=["pipelines"])
