from flask import Blueprint, request, jsonify, render_template
from src.databases import Review, db


review = Blueprint('review', __name__, url_prefix='/api/review')


@review.route('/get_all_reviews')
def get_all_reviews(): 
    reviewlist = Review.query.all()
    if len(reviewlist):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "review": [review.json() for review in reviewlist]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no reviews."
        }
    ), 404


@review.route('/get_review_by_id/<int:CPID>')
def get_review_by_id(CPID):
    review = Review.query.filter_by(CPID=CPID).first()
    if review:
        return jsonify(
            {
                "code": 200,
                "data": review.json()
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "Review not found."
        }
    ), 404

@review.route("/update_review/<int:CPID>", methods=['PUT'])
def update_review(CPID):
    try:
        review = Review.query.filter_by(CPID=CPID).first()
        if not review:
            return jsonify(
                {
                    "code": 404,
                    "data": {
                        "CPID": CPID
                    },
                    "message": "Review not found."
                }
            ), 404

         # update multiple columns
        data = request.get_json()
        if 'PRating' in data:
            review.PRating = data['PRating']
        if 'PDescription' in data:
            review.PDescription = data['PDescription']

        if 'DRating' in data:
            review.DRating = data['DRating']
        if 'DDescription' in data:
            review.DDescription = data['DDescription']

        db.session.commit()

        return jsonify(
            {
                "code": 200,
                "data": review.json()
            }
        ), 200
    except Exception as e:
        return jsonify(
            {
                "code": 500,
                "data": {
                    "CPID": CPID
                },
                "message": "An error occurred while updating the review. " + str(e)
            }
        ), 500

@review.route('/add_review/<int:CPID>', methods=['POST'])
def add_review(CPID):
    if (Review.query.filter_by(CPID=CPID).first()):
        return jsonify(
            {
                "code": 400,
                "data": {
                    "CPID": CPID
                },
                "message": "Review already exists."
            }
        ), 400

    data = request.get_json()
    review = Review(CPID, **data)

    try:
        db.session.add(review)
        db.session.commit()
    except:
        return jsonify(
            {
                "code": 500,
                "data": {
                    "CPID": CPID
                },
                "message": "An error occurred creating the review."
            }
        ), 500

    return jsonify(
        {
            "code": 200,
            "data": {
                'status': "Review has been added successfully."
            }
        }
    )
    
