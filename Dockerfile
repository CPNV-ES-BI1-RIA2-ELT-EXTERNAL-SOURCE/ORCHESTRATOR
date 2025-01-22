FROM python:3.12.6-slim

WORKDIR /orchestrator

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY Pipfile Pipfile.lock /orchestrator/

RUN pip install --no-cache-dir pipenv && \
    pipenv install --deploy

COPY . /orchestrator

EXPOSE 8000

CMD ["pipenv", "run", "fastapi", "run"]