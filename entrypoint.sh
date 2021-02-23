#!/bin/sh

python manage.py migrate --no-input
python manage.py compilemessages
python manage.py collectstatic --no-input

python manage.py runserver 0.0.0.0:8000