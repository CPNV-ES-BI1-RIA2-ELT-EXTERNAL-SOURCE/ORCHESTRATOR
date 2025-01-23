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
[![PyTest][PyTest]][PyTest-url]
[![Docker][Docker]][Docker-url]

## Getting Started

### Prerequisites

You firstly have to install Python and PipEnv on your machine.

To do so, you can follow the instructions on the [official Python website][Python-url] and on the [official pipenv website][Pipenv-url].

### Installation

#### Install Python

Follow the [official Python installation documentation][Python-download-url] to install Python on your machine.

#### Install Pip

Follow the [official Pip installation documentation][Pip-download-url] to install Pip on your machine.

#### Install PipEnv

You can follow these instructions to install PipEnv on your machine:

> Note: If you have any issues with the installation, you can refer to the [official PipEnv installation documentation][Pipenv-download-url].

```sh
pip install pipenv
```

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

## Docker

### Prerequisites

You firstly have to install Docker on your machine.

To do so, you can follow the instructions on the [official Docker website](https://docs.docker.com/get-docker/).

Before building the Docker image, you have to create a `config.yaml` file in the root directory of the project. Copy the content of the `config.example.yaml` file and fill in the required information.
You can find more information about the configuration in the [wiki](https://github.com/CPNV-ES-BI1-RIA2-ELT-EXTERNAL-SOURCE/ORCHESTRATOR/wiki/Configuration).

> Optionally, you can also map the `config.yaml` file to the Docker container by adding the following argument to the `docker run` command:
> 
> ```sh
> -v /path/to/config.yaml:/orchestrator/config.yaml
> ```

### Build the image

To build the Docker image, you can run the following command:

```sh
docker build -t orchestrator .
```

### Run the container

To run the Docker container, you can run the following command:

```sh
docker run -d -p 8000:8000 orchestrator
```

### Docker compose file

You can also use the `docker-compose.yml` file to build and run the Docker container. To do so, you can run the following command:

```sh
docker-compose up -d
```

## API Documentation

FastAPI provides an interactive API documentation based on OpenAPI that can be accessed on the route `/docs`.
You'll be able to see all the available endpoints and test them there.

## Collaborate

To collaborate on the project, the following conventions must be followed:
- [Gitflow conventions](https://www.atlassian.com/fr/git/tutorials/comparing-workflows/gitflow-workflow) are used for the management of branches.
- Commits follow the [Conventional Commits][conventionnal-commits-url] standard.
  - Here's a list of commit types that are used but not forced by the standard:
    - `docs: documentation change only`
    - `chore: changes to auxiliary tools and libraries`
- Communications are being conducted in our Discord server.

### Convention

The project uses the [Python coding conventions][PEP8-url].

#### Workflow

The project uses [Gitflow][GitFlow-url]. The branches used are: `main`, `develop`, `feature`, `release`, `hotfix`. The branches are named with the following pattern: `type/short-description` eg.(feature/awsome-feature).

## Directory Structure

```sh
┣ app/
┃ ┣ errors/
┃ ┣ helpers/
┃ ┣ routes/
┃ ┗ services/
┃ docs/
┗ tests/
  ┗ data/

```

## License

Distributed under the MIT License. See [`LICENSE.txt`](https://github.com/CPNV-ES-BI1-RIA2-ELT-EXTERNAL-SOURCE/ORCHESTRATOR/blob/develop/LICENSE.txt) for more information.

## Contact

You can contact any member of the team via discord on the class server([SI-T2a][Discord-url]).

[Python]: https://img.shields.io/badge/Python%203.12-000000?style=for-the-badge&logo=python&logoColor=python
[Python-url]: https://www.python.org/
[Python-download-url]: https://www.python.org/downloads/
[FastAPI]: https://img.shields.io/badge/FastAPI-000000?style=for-the-badge&logo=fastapi
[FastAPI-url]: https://fastapi.tiangolo.com/
[Pipenv]: https://img.shields.io/badge/PipEnv%202023.12.1-000000?style=for-the-badge&logo=python&logoColor=pipenv
[Pipenv-url]: https://pipenv.pypa.io/en/latest/
[GitFlow-url]: https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow
[Pip-download-url]: https://pip.pypa.io/en/stable/installation/
[PyTest]: https://img.shields.io/badge/PyTest-000000?style=for-the-badge&logo=python&logoColor=pytest
[PyTest-url]: https://docs.pytest.org/en/stable/
[PEP8-url]: https://peps.python.org/pep-0008/
[Discord-url]: https://discord.com/channels/1146349744822693899/1303407014122360943
[Pipenv-download-url]: https://pipenv.pypa.io/en/latest/installation.html
[conventionnal-commits-url]: https://www.conventionalcommits.org/en/v1.0.0/#specification
[Docker]: https://img.shields.io/badge/Docker-000000?style=for-the-badge&logo=docker&logoColor=docker
[Docker-url]: https://www.docker.com/