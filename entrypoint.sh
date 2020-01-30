#!/bin/sh

export FLASK_APP=src/app.py
export FLASK_ENV=development
python src/manage.py run -h 0.0.0.0 -p 5000
