#!/usr/bin/env bash
set -ae

export DATABASE_URL=postgres://postgres:postgres@db:5432/postgres

export REDIS_URL=redis://redis:6379/0

export RABBIT_URL=amqp://guest:guest@rabbitmq:5672/default

export BROKER_URL=${RABBIT_URL}

exec "$@"
