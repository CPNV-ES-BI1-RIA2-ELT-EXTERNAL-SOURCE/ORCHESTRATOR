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
        pipeline = self._get_pipeline(self._pipelines, pipeline_type)

        if pipeline is None:
            raise UnknownPipelineType(pipeline_type)

        current_job_id = self._get_job_id()

        async with httpx.AsyncClient() as client:
            for step in pipeline["steps"]:
                step_name = step["name"]
                hostname = step["hostname"]
                contactURL = step["contactURL"]
                method = step["method"].upper()

                try:
                    if method == "GET":
                        self._next_step_download_url = await self._get_download_url(
                            client, hostname, contactURL, current_job_id
                        )
                    elif method == "POST":
                        payload = {}

                        if "payload" in step:
                            payload = step["payload"]

                        self._next_step_download_url = (
                            await self._start_microservice_process(
                                client, hostname, contactURL, current_job_id, payload
                            )
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
        available_vars = {"job_id": job_id, "hostname": hostname}

        url = self._replace_placeholders(contactURL, available_vars)

        response = await client.get(url)
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
        payload: dict,
    ) -> None:
        available_vars = {"job_id": job_id, "hostname": hostname}

        if payload:
            payload = self._replace_placeholders(payload, available_vars)

        url = self._replace_placeholders(contactURL, available_vars)

        response = await client.post(
            url,
            json=payload,
        )

        if response.status_code != 200:
            raise HTTPException(
                status_code=response.status_code,
                detail="Failed to start microservice process",
            )

        return response.json().get("dataSource")

    def _get_job_id(self) -> int:
        return self.job_helper.get_job_id()

    def _get_pipeline(self, pipelines: dict, pipeline_type: str) -> list:
        return next((obj for obj in pipelines if obj["name"] == pipeline_type), None)

    def _replace_placeholders(self, data: dict, vars: dict) -> dict:
        if isinstance(data, dict):
            return {
                key: self._replace_placeholders(value, vars)
                for key, value in data.items()
            }
        elif isinstance(data, str):
            return data.format(**vars)
        else:
            return data
