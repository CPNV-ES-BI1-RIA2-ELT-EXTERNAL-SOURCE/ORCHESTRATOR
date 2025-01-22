Feature: Orchestrator run_pipeline

  Scenario: Successfully running a pipeline with a GET method
    Given the pipeline type is "data_pipeline"
    And the pipeline configuration exists with a GET method
    And the JobHelper is mocked to return job id 123
    When the pipeline is run
    Then the next step download URL should be fetched

  Scenario: Successfully running a pipeline with a POST method
    Given the pipeline type is "data_pipeline"
    And the pipeline configuration exists with a POST method
    And the JobHelper is mocked to return job id 123
    When the pipeline is run
    Then a POST request to the microservice should be made with the correct data