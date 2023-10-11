FROM python:3.11-slim-buster

COPY routers /backend/routers
COPY schemas /backend/schemas
COPY database /backend/database
COPY app.py /backend/app.py
COPY __init__.py /backend/__init__.py
COPY requirements.txt ./requirements.txt

RUN python3.11 -m pip install -r requirements.txt supervisor

CMD ["uvicorn", "backend.app:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "4567"]