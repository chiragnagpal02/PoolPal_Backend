from flask import Flask
from src.trial import tryme

def create_app():
    app = Flask(__name__)

    app.register_blueprint(tryme)
    return app