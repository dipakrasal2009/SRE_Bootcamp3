FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install Postgres client for pg_isready
RUN apt-get update && apt-get install -y postgresql-client && rm -rf /var/lib/apt/lists/*

COPY . .

RUN chmod +x entrypoint.sh

RUN cd ..

EXPOSE 5050

CMD ["/app/entrypoint.sh"]

