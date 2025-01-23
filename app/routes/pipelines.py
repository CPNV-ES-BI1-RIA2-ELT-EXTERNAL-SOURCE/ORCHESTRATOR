from fastapi import APIRouter, HTTPException
from app.services.orchestrator import Orchestrator

router = APIRouter()


@router.post("/start/{pipeline_type}", response_model=dict)
async def start_pipeline_type(pipeline_type: str):
    """
    This endpoint starts a specified data pipeline.
    
    Args:
    - pipeline_type: The type of pipeline to start.

    Returns:
    - A response indicating the status.
    """
    try:
        orchestrator = Orchestrator("config.yaml")
        await orchestrator.run_pipeline(pipeline_type)
        return {"status": "success"}
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
