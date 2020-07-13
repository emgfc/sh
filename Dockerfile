FROM python:3.8.1-slim-buster

WORKDIR /usr/src/sh-www

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y netcat

RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/sh-www/requirements.txt
RUN pip install -r requirements.txt

COPY . /usr/src/sh-www/

ENTRYPOINT ["/usr/src/sh-www/entrypoint.sh"]
