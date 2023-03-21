from flask import Blueprint, request, jsonify, render_template
from src.databases import Staff, db


staff = Blueprint('staff', __name__, url_prefix='/api/staff')


@staff.route('/get_all_staff')
def get_all_staff(): 
    stafflist = Staff.query.all()
    if len(stafflist):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "staff": [staff.json() for staff in stafflist]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no staff."
        }
    ), 404


@staff.route('/get_staff_by_id/<int:SID>')
def get_staff_by_id(CPID):
    staff = Staff.query.filter_by(SID=SID).first()
    if staff:
        return jsonify(
            {
                "code": 200,
                "data": staff.json()
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "Staff not found."
        }
    ), 404

@staff.route("/update_review/<int:SID>", methods=['PUT'])
def update_staff(SID):
    try:
        staff = Staff.query.filter_by(SID=SID).first()
        if not staff:
            return jsonify(
                {
                    "code": 404,
                    "data": {
                        "SID": SID
                    },
                    "message": "Staff not found."
                }
            ), 404

         # update multiple columns
        data = request.get_json()
        if 'SName' in data:
            staff.SName = data['SName']

        db.session.commit()

        return jsonify(
            {
                "code": 200,
                "data": staff.json()
            }
        ), 200
    except Exception as e:
        return jsonify(
            {
                "code": 500,
                "data": {
                    "SID": SID
                },
                "message": "An error occurred while updating the staff details. " + str(e)
            }
        ), 500

@staff.route('/add_staff/<int:SID>', methods=['POST'])
def add_staff(SID):
    data = request.get_json()
    staff = Staff(**data)

    try:
        db.session.add(staff)
        db.session.commit()
    except:
        return jsonify(
            {
                "code": 500,
                "message": "An error occurred creating the staff."
            }
        ), 500

    return jsonify(
        {
            "code": 201,
            "data": staff.json()
        }
    ), 201
    
