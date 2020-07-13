#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for Postgres to start..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "Postgres started"
fi

if [ $FLASK_ENV = "development" ]
then
  echo "Creating database schema"
  python manage.py create_db
  echo "Done"
fi

exec "$@"