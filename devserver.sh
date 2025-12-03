#!/bin/sh
source .venv/bin/activate
python backend_lavanderia/manage.py runserver $PORT
