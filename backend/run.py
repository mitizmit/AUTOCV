from flask import Flask
from dotenv import load_dotenv
import os
from app.routes.cv import cv_bp

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")

app.register_blueprint(cv_bp, url_prefix="/api")

if __name__ == "__main__":
    app.run(debug=True)
