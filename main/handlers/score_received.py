from peewee import DoesNotExist
from flask import jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from main.db.models.User import User
from main import app


@app.route("/score-received", methods=["GET"])
@jwt_required()
def score_received():
    current_username = get_jwt_identity()
    try:
        user = User.get(User.username == current_username)

    except DoesNotExist:
        return jsonify({"error": 1, "msg": "Username was not exist!"}), 400

    return (
        jsonify(
            {
                "max_easy": user.max_easy,
                "max_medium": user.max_medium,
                "max_hard": user.max_hard,
                "score_received": user.score_received,
                "msg": "Score received gave successfully.",
            }
        ),
        200,
    )
