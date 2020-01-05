
#!/bin/sh
set -o errexit
set -o nounset

python /app/manage.py collectstatic --noinput
uvicorn {{ cookiecutter.repo_name }}.asgi:application --chdir=/app