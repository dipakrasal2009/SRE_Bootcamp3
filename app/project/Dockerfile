FROM python:3.11-slim
WORKDIR /app
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get update && apt-get install -y postgresql-client && rm -rf /var/lib/apt/lists/*
COPY app/* .
RUN chmod +x entrypoint.sh
EXPOSE 5050
CMD ["entrypoint.sh"]

