from flask import Flask, jsonify
from .config import Config
from .db import db
from .routes import student_bp

def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    app.register_blueprint(student_bp)

    @app.route("/healthcheck")
    def healthcheck():
        return jsonify({"status": "healthy"}), 200

    return app

