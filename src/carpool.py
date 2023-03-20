from flask import Blueprint, request, jsonify, render_template
from src.databases import Carpool

carpool = Blueprint('carpool', __name__, url_prefix='/api/carpool')


@carpool.route("/carpool")
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