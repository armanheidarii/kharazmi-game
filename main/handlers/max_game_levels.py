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

    max_level1_score = user.games.select(fn.MAX(Game.level1_score)).scalar() or 0
    max_level2_score = user.games.select(fn.MAX(Game.level2_score)).scalar() or 0
    max_level3_score = user.games.select(fn.MAX(Game.level3_score)).scalar() or 0
    max_level4_score = user.games.select(fn.MAX(Game.level4_score)).scalar() or 0

    return (
        jsonify(
            {
                "max_level1_score": max_level1_score,
                "max_level2_score": max_level2_score,
                "max_level3_score": max_level3_score,
                "max_level4_score": max_level4_score,
                "msg": "Max game levels gave successfully.",
            }
        ),
        200,
    )
