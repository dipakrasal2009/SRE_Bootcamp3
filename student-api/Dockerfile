FROM python:3.11-slim

WORKDIR /app
#COPY . .
ENV PYTHONUNBUFFERED=1

# Install build dependencies for psycopg2
RUN apt-get update && \
    apt-get install -y  curl build-essential libpq-dev postgresql-client && \
    rm -rf /var/lib/apt/lists/*

COPY requirement.txt .
RUN pip install --no-cache-dir -r requirement.txt

# Copy application code
COPY . .

# Expose API port
EXPOSE 5050

# Production entry point: Gunicorn with 4 workers
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5050", "app:create_app()"]

