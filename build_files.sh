#!/usr/bin/env bash

echo "Building project packages..."
python3 -m pip install -r requirements.txt

echo "Migrating Database..."
# apt-get update && apt-get install -y sqlite3 libsqlite3-dev
# python3 manage.py makemigrations --noinput
# python3 manage.py migrate --noinput

echo "Collectiong static files..."
# python3 manage.py collectstatic --noinput