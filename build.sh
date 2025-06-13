#!/bin/bash

echo "🔧 Iniciando processo de build para aplicação Django..."

# Instala pipenv
pip install pipenv

# Instala as dependências declaradas no Pipfile.lock
pipenv install --deploy --ignore-pipfile

# Aplica migrações do banco de dados
pipenv run python manage.py migrate

# Coleta arquivos estáticos
pipenv run python manage.py collectstatic --noinput

# Cria superusuário (com lógica definida no comando createadmin)
pipenv run python manage.py createadmin
