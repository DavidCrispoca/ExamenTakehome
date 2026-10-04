FROM python:3.12

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY backend/ ./app/

EXPOSE 8105

CMD ["sh", "-c", "uvicorn app.main:app --host 0.0.0.0 --port ${APP_PORT:-8105}"]
