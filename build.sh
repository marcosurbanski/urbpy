#!/bin/bash

# Instala dependências
pip install pipenv
pipenv install --deploy --ignore-pipfile

# Roda as migrações
pipenv run python manage.py migrate

# Executa o collectstatic
pipenv run python manage.py collectstatic --noinput

# Cria superusuário, se não existir
pipenv run python manage.py createadmin
