from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

# Create a passenger DB and a Driver DB and a Carpool DB


# Passenger DB

class Passengers(db.Model):
    PID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    PName = db.Column(db.String(200), nullable=False)
    PAge = db.Column(db.Integer, nullable=False)
    PGender = db.Column(db.String(1), nullable=False)
    PEmail = db.Column(db.String(200), nullable=False)
    PAddress = db.Column(db.String(400), nullable=False)
    PPhone = db.Column(db.Integer, nullable=False)
    PAccount_Created_At = db.Column(db.DateTime, default=datetime.now())
    
    
    def __repr__(self) -> str:
        return f'Request >>> {self.project}'
