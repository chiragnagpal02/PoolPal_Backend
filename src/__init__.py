from flask import Flask
from src.trial import tryme

# from src.databases import db
from src.auth import auth
import os

def create_app():
    app = Flask(__name__)

    app.config.from_mapping(
        SECRET_KEY='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',
        SQLALCHEMY_DATABASE_URI=os.environ.get("SQLALCHEMY_DATABASE_URI")
    )

    # db.app = app
    # db.init_app(app)

    app.register_blueprint(tryme)
    
    app.register_blueprint(auth)

    return app