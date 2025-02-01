from peewee import fn, DoesNotExist
from flask import jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from main.db.models.User import User
from main import app


@app.route("/games-count", methods=["GET"])
@jwt_required()
def games_count():
    current_username = get_jwt_identity()
    try:
        user = User.get(User.username == current_username)

    except DoesNotExist:
        return jsonify({"error": 1, "msg": "Username was not exist!"}), 400

    return (
        jsonify(
            {
                "games_count": user.games.count(),
                "msg": "Games count gave successfully.",
            }
        ),
        200,
    )
