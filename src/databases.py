from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

# Create a passenger DB and a Driver DB and a Carpool DB
class Carpool(db.Model):
    __tablename__ = 'carpooling'

    CPID = db.Column(db.String(13), primary_key=True, autoincrement=True)
    PID = db.Column(db.String(64), nullable=False)
    DID = db.Column(db.Integer, nullable=False)
    DriverFee = db.Column(db.Float(precision=2), nullable=False)
    DateTime = db.Column(db.DateTime, default=datetime.now())
    CPStartLocation = db.Column(db.String(64), nullable=False)
    CPendLocation = db.Column(db.String(64), nullable=False)
    Status = db.Column(db.String(64), nullable=False)
    Price = db.Column(db.Float(precision=2), nullable=False)

class Driver(db.Model):
    __tablename__ = 'driver'

    DID = db.Column(db.Float(precision=2), nullable=False, autoincrement=True)
    DName = db.Column(db.String(64), nullable=False)
    DAge = db.Column(db.Integer, nullable=False)
    DGender = db.Column(db.String(1), nullable=False)
    DEmail = db.Column(db.String(64), nullable=False)
    DVehicleNo = db.Column(db.String(64), nullable=False)
    DLicenseNo = db.Column(db.String(64), nullable=False)
    DPhoneNo = db.Column(db.String(8), nullable=False)

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



