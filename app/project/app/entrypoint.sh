#!/bin/bash
echo "Starting Flask app..."
export FLASK_APP=app:app
exec flask run --host=0.0.0.0 --port=5050

