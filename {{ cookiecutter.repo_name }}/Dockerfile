FROM python:3.6.5
ENV PYTHONUNBUFFERED 1

RUN pip install pipenv

RUN mkdir /app
WORKDIR /app

ADD Pipfile /app/Pipfile
ADD Pipfile.lock /app/Pipfile.lock

RUN pipenv install --system --deploy

ADD . /app/

COPY ./docker/django/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
