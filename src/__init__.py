from flask import Flask
from src.trial import tryme
from src.databases import db
import os

def create_app():
    app = Flask(__name__)

    app.config.from_mapping(
        SECRET_KEY='dev',
        SQLALCHEMY_DATABASE_URI=os.environ.get("SQLALCHEMY_DATABASE_URI")
    )

    db.app = app
    db.init_app(app)

    app.register_blueprint(tryme)

    return app