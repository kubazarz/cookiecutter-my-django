from .base import *  # noqa


DEBUG = env.bool('DJANGO_DEBUG', default=True)
TEMPLATES[0]['OPTIONS']['debug'] = DEBUG

SECRET_KEY = env("DJANGO_SECRET_KEY", default='CHANGEME!!!')
