#!/bin/bash
pip install pipenv
pipenv install --deploy --ignore-pipfile

# Executa o collectstatic
pipenv run python manage.py collectstatic --noinput
