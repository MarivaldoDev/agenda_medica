#!/bin/sh

set -e

echo "Aplicando migrações..."
flask db upgrade

echo "Populando banco de dados..."
flask seed

echo "Iniciando aplicação..."
exec flask --app run run --host=0.0.0.0