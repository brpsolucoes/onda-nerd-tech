#!/bin/bash
set -e # Para o script se algum comando falhar

echo "--> Rodando Migrations..."
python manage.py migrate --no-input

echo "--> Coletando Static Files..."
python manage.py collectstatic --no-input

echo "--> Iniciando Gunicorn..."
exec gunicorn --workers 3 --bind 0.0.0.0:8000 config.wsgi:application