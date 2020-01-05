import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', '{{ cookiecutter.repo_name }}.settings.local')

app = Celery('{{ cookiecutter.repo_name }}')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
