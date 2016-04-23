import os
import shutil


PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_api_module(project_directory):
    api_module_location = os.path.join(project_directory, 'api')
    shutil.rmtree(api_module_location)


if '{{ cookiecutter.use_django_rest_framework }}'.lower() != 'y':
    remove_api_module(PROJECT_DIRECTORY)
