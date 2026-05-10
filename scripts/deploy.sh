#!/bin/bash

DEPLOY_PATH=/home/bjptechn/bjp-technologies-web
VENV=/home/bjptechn/virtualenv/bjp-technologies-web/3.12/bin
LOG=/tmp/bjp_deploy.log

echo "=== Deploy started: $(date) ===" >> "$LOG"

cd "$DEPLOY_PATH" || exit 1

git pull origin main >> "$LOG" 2>&1
"$VENV/pip" install -r requirements.txt --quiet >> "$LOG" 2>&1
DJANGO_SETTINGS_MODULE=config.settings.production "$VENV/python" manage.py migrate --no-input >> "$LOG" 2>&1
DJANGO_SETTINGS_MODULE=config.settings.production "$VENV/python" manage.py collectstatic --no-input >> "$LOG" 2>&1
touch tmp/restart.txt

echo "=== Deploy complete: $(date) ===" >> "$LOG"
