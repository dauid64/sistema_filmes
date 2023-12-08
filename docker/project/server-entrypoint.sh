#!/bin/sh

until cd /app/project
do
    echo "Waiting for server volume..."
done


until python manage.py migrate
do
    echo "Waiting for db to be ready..."
    sleep 2
done

export DJANGO_SUPERUSER_EMAIL=admin@gmail.com
export DJANGO_SUPERUSER_USERNAME=admin
export DJANGO_SUPERUSER_PASSWORD=123
python manage.py createsuperuser --noinput

python manage.py migrate --noinput

python manage.py collectstatic --noinput

gunicorn project.wsgi --bind 0.0.0.0:8000 --workers 4 --threads 4

# for debug
#python manage.py runserver 0.0.0.0:8000