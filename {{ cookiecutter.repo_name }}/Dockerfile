FROM python:3.8.1-alpine3.11

ARG DJANGO_ENV

ENV PYTHONUNBUFFERED=1 \
    DJANGO_ENV=${DJANGO_ENV} \
    POETRY_VERSION=1.0.0

RUN apk --no-cache add \
    build-base \
    libffi-dev \
    gcc \
    git \
    gettext \
    musl-dev \
    postgresql-dev \
    libtool \
    cmake \
    autoconf \
    automake \
    tini \
 && pip install "poetry==$POETRY_VERSION"

RUN mkdir /app
WORKDIR /app

COPY poetry.lock pyproject.toml /app/

RUN poetry config virtualenvs.create false \
 && poetry install $(test "$DJANGO_ENV" == production && echo "--no-dev") --no-root

COPY ./docker/django/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
COPY ./docker/django/uvicorn.sh /uvicorn.sh
RUN chmod +x /uvicorn.sh

ADD . /app/

ENTRYPOINT ["/sbin/tini", "--", "/entrypoint.sh"]