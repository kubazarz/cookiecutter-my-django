FROM python:3.7
ENV PYTHONUNBUFFERED 1

RUN pip install 'pip==18.0' 'pipenv==2018.7.1'

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
ENTRYPOINT ["/entrypoint.sh"]
