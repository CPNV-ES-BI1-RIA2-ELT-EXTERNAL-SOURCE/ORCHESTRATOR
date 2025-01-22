import httpx

from fastapi import HTTPException

from app.errors.unknown_pipeline_type import UnknownPipelineType
from app.helpers import load_config, JobHelper


class Orchestrator:
    def __init__(
        self, config_file_path: str, metadata_file_path: str = "metadata.yaml"
    ):
        self.job_helper = JobHelper(metadata_file_path)

        self._pipelines = load_config(config_file_path, "pipelines")

        self._next_step_download_url = None

    async def run_pipeline(self, pipeline_type: dict) -> None:
        pipelines = self._pipelines

        pipeline = next(
            (p[pipeline_type] for p in pipelines if pipeline_type in p), None
        )

        if pipeline is None:
            raise UnknownPipelineType(pipeline_type)

        current_job_id = self._get_job_id()

        async with httpx.AsyncClient() as client:
            for step in pipeline:
                step_name, service = list(step.items())[0]
                hostname = service["hostname"]
                contactURL = service["contactURL"]
                method = service["method"].upper()

                try:
                    if method == "GET":
                        self._next_step_download_url = await self._get_download_url(
                            client, hostname, contactURL, current_job_id
                        )
                    elif method == "POST":
                        payload = {}

                        if "payload" in service:
                            payload = service["payload"]
                        await self._start_microservice_process(
                            client, hostname, contactURL, current_job_id, payload
                        )
                    else:
                        raise ValueError(f"Unsupported HTTP method: {method}")

                except httpx.HTTPStatusError as e:
                    raise HTTPException(
                        status_code=e.response.status_code, detail=str(e)
                    )
                except Exception as e:
                    raise HTTPException(
                        status_code=500, detail=f"Error with {step_name}: {str(e)}"
                    )

    async def _get_download_url(
        self, client: httpx.AsyncClient, hostname: str, contactURL: str, job_id: int
    ) -> str:
        response = await client.get(f"http://{hostname}{contactURL}/{job_id}")
        if response.status_code != 200:
            raise HTTPException(
                status_code=response.status_code,
                detail="Failed to call download service",
            )
        return response.json().get("url")

    async def _start_microservice_process(
        self,
        client: httpx.AsyncClient,
        hostname: str,
        contactURL: str,
        job_id: int,
        payload: dict = None,
    ) -> None:
        response = await client.post(
            f"http://{hostname}{contactURL}/{job_id}",
            json=payload,
        )
        if response.status_code != 200:
            raise HTTPException(
                status_code=response.status_code,
                detail="Failed to start microservice process",
            )

    def _get_job_id(self) -> int:
        return self.job_helper.get_job_id()
