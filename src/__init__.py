from flask import Flask
from src.trial import tryme
from src.stripe import payment
from src.databases import db
from src.auth import auth
from src.carpool import carpool
from src.driver import driver
from src.passenger import passenger
from src.googlemap import googleMap
import os

def create_app():
    app = Flask(__name__)

    app.config.from_mapping(
        SECRET_KEY='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',
        SQLALCHEMY_DATABASE_URI=os.environ.get("SQLALCHEMY_DATABASE_URI")
    )

    db.app = app
    db.init_app(app)

    app.register_blueprint(driver)
    app.register_blueprint(passenger)
    app.register_blueprint(carpool)
    app.register_blueprint(tryme)
    app.register_blueprint(payment)
    app.register_blueprint(auth)
    app.register_blueprint(googleMap)

    return app