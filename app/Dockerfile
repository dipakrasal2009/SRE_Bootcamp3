FROM python:3.11-slim

WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the code
COPY . .

EXPOSE 8081

ENV FLASK_APP=__init__.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=8081

# Add entrypoint script
RUN chmod +x /app/entrypoint.sh

CMD ["/app/entrypoint.sh"]

#CMD ["flask", "run"]

