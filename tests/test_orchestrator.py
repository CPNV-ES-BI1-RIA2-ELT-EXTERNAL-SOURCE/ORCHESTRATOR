import pytest
from pytest_bdd import scenarios, given, when, then
from unittest.mock import patch, AsyncMock

from app.services.orchestrator import Orchestrator
from app.helpers import JobHelper

scenarios("run_pipeline.feature")

# Fixtures


@pytest.fixture
def orchestrator():
    return Orchestrator(
        config_file_path="config.yaml", metadata_file_path="metadata.yaml"
    )


@pytest.fixture
def mock_load_config():
    with patch("app.services.orchestrator.load_config") as mock:
        mock.return_value = [
            {
                "data_pipeline": [
                    {
                        "step1": {
                            "hostname": "localhost",
                            "contactURL": "/geturl",
                            "method": "GET",
                        }
                    }
                ]
            },
            {
                "data_pipeline": [
                    {
                        "step1": {
                            "hostname": "localhost",
                            "contactURL": "/startprocess",
                            "method": "POST",
                        }
                    }
                ]
            },
        ]
        yield mock


@pytest.fixture
def mock_job_helper():
    with patch.object(JobHelper, "get_job_id", return_value=123):
        yield JobHelper(config_file="metadata.yaml")


@pytest.fixture
def mock_http_client():
    with patch("httpx.AsyncClient") as mock_client:
        mock_client.return_value.__aenter__.return_value = AsyncMock()
        yield mock_client


# Given Steps


@pytest.fixture
def pipeline_type():
    return "data_pipeline"


@given('the pipeline type is "data_pipeline"')
@given("the pipeline configuration exists with a GET method")
@given("the pipeline configuration exists with a POST method")
@given("the JobHelper is mocked to return job id 123")
# When Steps


@when("the pipeline is run")
async def run_pipeline(orchestrator, pipeline_type, mock_job_helper):
    await orchestrator.run_pipeline(pipeline_type)


# Then Steps


@then("the next step download URL should be fetched")
async def check_get_method_call(mock_http_client):
    mock_http_client.return_value.__aenter__.return_value.get.assert_called_once_with(
        "http://localhost/geturl/123"
    )


@then("a POST request to the microservice should be made with the correct data")
async def check_post_method_call(mock_http_client):
    mock_http_client.return_value.__aenter__.return_value.post.assert_called_once_with(
        "http://localhost/startprocess/123", json={"dataSource": None}
    )
