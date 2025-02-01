from peewee import DoesNotExist
from flask import jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from main.db.models.User import User
from main import app


@app.route("/get-rank", methods=["GET"])
@jwt_required()
def get_rank():
    current_username = get_jwt_identity()
    try:
        user = User.get(User.username == current_username)

    except DoesNotExist:
        return jsonify({"error": 1, "msg": "Username was not exist!"}), 400

    class_rank = (
        User.select()
        .where(
            (User.class_ref == user.class_ref)
            & (User.score_received > user.score_received)
        )
        .count()
    ) + 1
    overall_rank = (
        User.select().where(User.score_received > user.score_received).count() + 1
    )

    return (
        jsonify(
            {
                "class_rank": class_rank,
                "overall_rank": overall_rank,
                "msg": "Ranks gave successfully.",
            }
        ),
        200,
    )
