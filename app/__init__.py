from flask import Flask
from .config import Config
from .db import db
from flask_migrate import Migrate
# or wherever db is defined
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    #migrate = Migrate(app, db)
    from .routes import student_bp
    app.register_blueprint(student_bp)

    @app.route('/healthcheck')
    def healthcheck():
        return {"status": "healthy"}, 200
    return app
