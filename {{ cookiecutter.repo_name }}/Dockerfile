FROM python:3.7.1-alpine3.8
ENV PYTHONUNBUFFERED 1

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
    tini

RUN pip install 'pip==18.1' 'pipenv==2018.11.26'

RUN mkdir /app
WORKDIR /app

ADD Pipfile /app/Pipfile
ADD Pipfile.lock /app/Pipfile.lock

RUN pipenv install --system --deploy

ADD . /app/

COPY ./docker/django/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
COPY ./docker/django/uvicorn.sh /uvicorn.sh
RUN chmod +x /uvicorn.sh
ENTRYPOINT ["/sbin/tini", "--", "/entrypoint.sh"]
