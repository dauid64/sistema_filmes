#!/bin/sh

until cd /app/project
do
    echo "Waiting for server volume..."
done

# run a worker :)
celery -A project worker --loglevel=info --concurrency 1 -E
