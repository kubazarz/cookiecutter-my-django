#!/usr/bin/env bash
set -ae

export DATABASE_URL=postgis://postgres:postgres@db:5432/postgres

export REDIS_URL=redis://redis:6379/0

export BROKER_URL=${REDIS_URL}

exec "$@"
