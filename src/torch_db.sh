#!/usr/local/bin/bash

find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc"  -delete
rm -f db.sqlite3
python manage.py makemigrations
python manage.py migrate
<<<<<<< HEAD
=======
python manage.py createsuperuser --user admin
python manage.py loaddata workout/workout.yaml
>>>>>>> 7de5fc4
