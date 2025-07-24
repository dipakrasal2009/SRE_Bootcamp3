"""
Lightweight “migration” script that simply creates all tables.
Executed by the init-container in Kubernetes.
"""
from app import create_app
from .db import db

app = create_app()
with app.app_context():
    db.create_all()
    print("✔️  Database schema created")

