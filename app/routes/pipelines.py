from fastapi import APIRouter, HTTPException
from app.services import orchestrator

router = APIRouter()

orchestrator = orchestrator.Orchestrator("config.yaml")


@router.post("/start/{pipeline_type}", response_model=dict)
async def start_pipeline_type(pipeline_type: str):
    """
    This endpoint starts a specified data pipeline. There are two pipeline types:
    1. "data_lake_pipeline": Data Generator -> Extract -> Load -> Data Lake
    2. "database_pipeline": Transform -> Load -> Database

    Args:
    - pipeline_type: The type of pipeline to start ("data_lake_pipeline" or "database_pipeline").

    Returns:
    - A response indicating the status.
    """
    try:
        await orchestrator.run_pipeline(pipeline_type)
        return {"status": "success"}
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
