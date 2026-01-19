FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Render listens on port 10000 internally
EXPOSE 10000

CMD ["gunicorn", "app:app", "--workers=1", "--threads=1", "--bind=0.0.0.0:10000"]
