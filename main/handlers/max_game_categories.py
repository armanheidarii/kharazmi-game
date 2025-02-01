from peewee import fn, DoesNotExist
from flask import jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from main.db.models.User import User
from main.db.models.Game import Game
from main import app


@app.route("/max-game-categories", methods=["GET"])
@jwt_required()
def max_game_categories():
    current_username = get_jwt_identity()
    try:
        user = User.get(User.username == current_username)

    except DoesNotExist:
        return jsonify({"error": 1, "msg": "Username was not exist!"}), 400

    max_easy = (
        user.games.select(Game.final_score)
        .where(Game.game_level == 0)
        .order_by(Game.final_score.desc())
        .scalar()
        or 0
    )
    max_medium = (
        user.games.select(Game.final_score)
        .where(Game.game_level == 1)
        .order_by(Game.final_score.desc())
        .scalar()
        or 0
    )
    max_hard = (
        user.games.select(Game.final_score)
        .where(Game.game_level == 2)
        .order_by(Game.final_score.desc())
        .scalar()
        or 0
    )

    return (
        jsonify(
            {
                "max_easy": max_easy,
                "max_medium": max_medium,
                "max_hard": max_hard,
                "msg": "Max game categories gave successfully.",
            }
        ),
        200,
    )
