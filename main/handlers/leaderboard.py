from peewee import DoesNotExist
from flask import jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from main.db.models.User import User
from main import app


@app.route("/leaderboard", methods=["GET"])
@jwt_required()
def leaderboard():
    current_username = get_jwt_identity()
    try:
        user = User.get(User.username == current_username)

    except DoesNotExist:
        return jsonify({"error": 1, "msg": "Username was not exist!"}), 400

    class_leaderboard_users = (
        User.select(User.username, User.score_received)
        .where(User.class_ref == user.class_ref)
        .order_by(User.score_received.desc())
    )
    class_leaderboard = [
        {"username": user.username, "score_received": user.score_received}
        for user in class_leaderboard_users
    ]

    global_leaderboard_users = User.select(User.username, User.score_received).order_by(
        User.score_received.desc()
    )
    global_leaderboard = [
        {"username": user.username, "score_received": user.score_received}
        for user in global_leaderboard_users
    ]

    return (
        jsonify(
            {
                "class_leaderboard": class_leaderboard,
                "global_leaderboard": global_leaderboard,
                "msg": "Leaderboard received gave successfully.",
            }
        ),
        200,
    )
