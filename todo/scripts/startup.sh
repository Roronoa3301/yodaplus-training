#!/bin/bash


echo "running migrations"
python3 manage.py migrate


echo "bring up local server"
python3 manage.py runserver 0.0.0.0:8000