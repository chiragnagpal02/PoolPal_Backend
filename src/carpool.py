from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/carpool'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)
CORS(app)

class Carpool(db.Model):
    __tablename__ = 'carpool'

    CPID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    DID = db.Column(db.Integer, nullable=False)
    DateTime = db.Column(db.DateTime, default=datetime.now())
    CPStartLocation = db.Column(db.String(64), nullable=False)
    CPendLocation = db.Column(db.String(64), nullable=False)
    Status = db.Column(db.String(64), nullable=False)

    def __init__(self, cpid, did, datetime, startlocation, endlocation, status):
        self.CPID = cpid
        self.DID = did
        self.DateTime = datetime
        self.CPStartLocation = startlocation
        self.CPendLocation = endlocation
        self.Status = status


    def json(self):
        return {"CPID": self.CPID, "DID": self.DID, "DateTime": self.DateTime, "CPStartLocation": self.CPStartLocation, "CPendLocation" : self.CPendLocation, "Status" : self.Status}

@app.route("/carpool")
def get_all():
    carpoollist = Carpool.query.all()
    if len(carpoollist):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "Carpools": [carpool.json() for carpool in carpoollist]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no carpool."
        }
    ), 404