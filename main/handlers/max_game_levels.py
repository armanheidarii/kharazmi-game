from peewee import DoesNotExist
from flask import jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from main.db.models.User import User
from main import app


@app.route("/max-game-levels", methods=["GET"])
@jwt_required()
def max_game_levels():
    current_username = get_jwt_identity()
    try:
        user = User.get(User.username == current_username)

    except DoesNotExist:
        return jsonify({"error": 1, "msg": "Username was not exist!"}), 400

    return (
        jsonify(
            {
                "max_level1_score": user.max_level1_score,
                "max_level2_score": user.max_level2_score,
                "max_level3_score": user.max_level3_score,
                "max_level4_score": user.max_level4_score,
                "msg": "Max game levels gave successfully.",
            }
        ),
        200,
    )
