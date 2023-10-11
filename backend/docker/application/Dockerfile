FROM python:3.11-slim-buster

COPY routers /backend/routers
COPY schemas /backend/schemas
COPY database /backend/database
COPY app.py /backend/app.py
COPY __init__.py /backend/__init__.py
COPY config.py /backend/config.py
COPY .env /backend/.env
COPY requirements.txt ./requirements.txt
COPY alembic.ini ./alembic.ini

RUN python3.11 -m pip install -r requirements.txt supervisor
