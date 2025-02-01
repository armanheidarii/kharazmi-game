from peewee import fn, DoesNotExist
from flask import jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from main.db.models.User import User
from main.db.models.Game import Game
from main import app


@app.route("/max-game-levels", methods=["GET"])
@jwt_required()
def max_game_levels():
    current_username = get_jwt_identity()
    try:
        user = User.get(User.username == current_username)

    except DoesNotExist:
        return jsonify({"error": 1, "msg": "Username was not exist!"}), 400

    max_level1 = (
        Game.select(fn.MAX(Game.level1_score)).where(Game.user == user).scalar() or 0
    )
    max_level2 = (
        Game.select(fn.MAX(Game.level2_score)).where(Game.user == user).scalar() or 0
    )
    max_level3 = (
        Game.select(fn.MAX(Game.level3_score)).where(Game.user == user).scalar() or 0
    )
    max_level4 = (
        Game.select(fn.MAX(Game.level4_score)).where(Game.user == user).scalar() or 0
    )

    return (
        jsonify(
            {
                "max_level1": max_level1,
                "max_level2": max_level2,
                "max_level3": max_level3,
                "max_level4": max_level4,
                "msg": "Max game levels gave successfully.",
            }
        ),
        200,
    )
