from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="Orchestrator", version="0.0.1")
app.include_router(router.api_router)
