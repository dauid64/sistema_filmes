FROM python:3.11.3-alpine3.18

RUN apk update && apk add python3-dev gcc libc-dev

WORKDIR /app

RUN pip install --upgrade pip
RUN pip install gunicorn
ADD ./requirements.txt /app/
RUN pip install -r requirements.txt

ADD ./project /app/project
ADD ./docker /app/docker

RUN chmod +x /app/docker/project/server-entrypoint.sh
RUN chmod +x /app/docker/project/worker-entrypoint.sh
