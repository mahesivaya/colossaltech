#!/bin/bash
python3.11 manage.py collectstatic && gunicorn --workers 2 myproject.wsgi
