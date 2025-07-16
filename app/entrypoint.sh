#!/bin/bash
echo "Waiting for database to be ready..."
sleep 5  # wait for DB container to start

echo "Running DB migrations..."
python -c "from app import create_app; from app.db import db; app = create_app(); \
with app.app_context(): db.create_all()"

echo "Starting Flask app..."
exec flask run --host=0.0.0.0 --port=5000

