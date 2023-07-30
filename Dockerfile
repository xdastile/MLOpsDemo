# docker build -t modelimage .
# docker run modelimage

#build and remove intermediate containers
# docker build --rm -t modelimage .

#run container in background
# docker run -d modelimage

#run container in background with port mapping
# docker run -d -p 5000:5000 modelimage

FROM python:3.8-slim as builder

ENV POETRY_VERSION=1.5.1

# Install dependencies required for installing packages
RUN export DEBIAN_FRONTEND=noninteractive \
    && apt-get -qq update \
    && apt-get -qq install -y curl build-essential cmake libboost-all-dev \
    && rm -rf /var/lib/apt/lists/*

# Create a virtualenv and install poetry
RUN python -m venv /venv \
    && /venv/bin/pip install -U pip setuptools \
    && /venv/bin/pip install poetry==${POETRY_VERSION}

ENV PATH="${PATH}:/venv/bin"

WORKDIR /app

COPY pyproject.toml ./pyproject.toml
COPY poetry.lock ./poetry.lock
RUN . /venv/bin/activate && poetry install

FROM python:3.8-slim as app

WORKDIR /app

COPY --from=builder /venv /venv
COPY ./src ./src
COPY ./model ./model
COPY docker-entrypoint.sh docker-entrypoint.sh

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED 1

RUN chmod +x docker-entrypoint.sh

CMD ["./docker-entrypoint.sh"]