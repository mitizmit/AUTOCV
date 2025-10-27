from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app)

    # Import i rejestracja blueprintów
    from .routes.cv import cv_bp
    from .routes.jobs import jobs_bp
    app.register_blueprint(cv_bp, url_prefix="/api/cv")
    app.register_blueprint(jobs_bp, url_prefix="/api/jobs")

    return app
