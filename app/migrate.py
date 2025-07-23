from db import db
from myapp import create_app

app = create_app()
with app.app_context():
    db.create_all()

