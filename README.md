<h3 align="center">Orchestrator</h3>

  <p align="center">
    <a href="https://github.com/CPNV-ES-BI1-SBB/EXTERNAL-SOURCE-TRANSFORM/wiki"><strong>Explore the docs</strong></a>
    <br />
  </p>
</div>

## About The Service

This service aims to orchestrate the different services of the project. It will be the entry point of the project and will manage the different requests. 

### Built With

[![Python][Python]][Python-url]
[![Pipenv][Pipenv]][Pipenv-url]
[![FastAPI][FastAPI]][FastAPI-url]

## Getting Started

### Prerequisites

You firstly have to install Python and PipEnv on your machine.

To do so, you can follow the instructions on the [official Python website][Python-url] and on the [official pipenv website][Pipenv-url].

### Installation

#### Development

1. Clone the repository

    ```sh
    git clone https://github.com/CPNV-ES-BI1-RIA2-ELT-EXTERNAL-SOURCE/ORCHESTRATOR.git
    ```

2. Install the dependencies

    ```sh
    pipenv shell
    pipenv install --dev
    ```

3. Run the service

    ```sh
    faststapi dev
    ```

#### Production

1. Clone the repository

    ```sh
    git clone https://github.com/CPNV-ES-BI1-RIA2-ELT-EXTERNAL-SOURCE/ORCHESTRATOR.git
    ```

2. Install the dependencies

    ```sh
    pipenv shell
    pipenv install
    ```

3. Run the service

    ```sh
    faststapi run
    ```

## API Documentation

FastAPI provides an interactive API documentation based on OpenAPI that can be accessed on the route `/docs`.
You'll be able to see all the available endpoints and test them there.

## Collaborate

### Convention

#### Commit

The project uses [Conventional Commits][Commit-url]. The keywords used are: `feat`, `fix`, `chore`, `refactor`, `test`, `docs`. The commits are named with the following pattern: `type: description` eg.(feat: add awsome feature).

#### Workflow

The project uses [Gitflow][GitFlow-url]. The branches used are: `main`, `develop`, `feature`, `release`, `hotfix`. The branches are named with the following pattern: `type/short-description` eg.(feature/awsome-feature).

#### file naming

The project uses [PEP8](https://peps.python.org/pep-0008) naming convention.

## Directory Structure

## License

Distributed under no license.

## Contact

You can contact any member of the team via discord on the class server(SI-T2a) in the #elt channel.

[Python]: https://img.shields.io/badge/Python%203.12-000000?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://www.python.org/
[FastAPI]: https://img.shields.io/badge/FastAPI-000000?style=for-the-badge&logo=fastapi
[FastAPI-url]: https://fastapi.tiangolo.com/
[Pipenv]: https://img.shields.io/badge/PipEnv%202023.12.1-000000?style=for-the-badge&logo=python&logoColor=white
[Pipenv-url]: https://pipenv.pypa.io/en/latest/
[GitFlow-url]: https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow
[Commit-url]: https://www.conventionalcommits.org/
