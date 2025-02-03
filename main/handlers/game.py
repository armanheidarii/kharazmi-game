from peewee import DoesNotExist
from flask import jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from main.db.models.User import User
from main.db.models.Game import Game
from main import app


@app.route("/game", methods=["POST"])
@jwt_required()
def game():
    current_username = get_jwt_identity()
    try:
        user = User.get(User.username == current_username)

    except DoesNotExist:
        return jsonify({"error": 1, "msg": "Username was not exist!"}), 400

    game_level = request.json.get("game_level")
    level1_score = request.json.get("level1_score")
    level2_score = request.json.get("level2_score")
    level3_score = request.json.get("level3_score")
    level4_score = request.json.get("level4_score")

    if game_level == None:
        return jsonify({"error": 2, "msg": "Game level cannot be empty!"}), 400

    if level1_score == None:
        return jsonify({"error": 3, "msg": "Level1 score cannot be empty!"}), 400

    if level2_score == None:
        return jsonify({"error": 4, "msg": "Level2 score cannot be empty!"}), 400

    if level3_score == None:
        return jsonify({"error": 5, "msg": "Level3 score cannot be empty!"}), 400

    if level4_score == None:
        return jsonify({"error": 6, "msg": "Level4 score cannot be empty!"}), 400

    if game_level < 0 or game_level > 2:
        return jsonify({"error": 7, "msg": "Game level is invalid!"}), 400

    if level1_score < 0 or level1_score > 10:
        return jsonify({"error": 8, "msg": "Level1 score is invalid!"}), 400

    if level2_score < 0 or level2_score > 3:
        return jsonify({"error": 9, "msg": "Level2 score is invalid!"}), 400

    if level3_score < 0:
        return jsonify({"error": 10, "msg": "Level3 score is invalid!"}), 400

    if level4_score < 0 or level4_score > 2:
        return jsonify({"error": 11, "msg": "Level4 score is invalid!"}), 400

    final_score = (
        level1_score + level2_score + level3_score + level4_score + 10 * game_level
    )

    game = Game.create(
        game_level=game_level,
        level1_score=level1_score,
        level2_score=level2_score,
        level3_score=level3_score,
        level4_score=level4_score,
        final_score=final_score,
        user=user,
    )

    if game_level == 0 and final_score > user.max_easy:
        user.max_easy = final_score
        user.score_received = user.max_easy + user.max_medium + user.max_hard
        user.save()
    elif game_level == 1 and final_score > user.max_medium:
        user.max_medium = final_score
        user.score_received = user.max_easy + user.max_medium + user.max_hard
        user.save()
    elif game_level == 2 and final_score > user.max_hard:
        user.max_hard = final_score
        user.score_received = user.max_easy + user.max_medium + user.max_hard
        user.save()

    if level1_score > user.max_level1_score:
        user.max_level1_score = level1_score
        user.save()
    if level2_score > user.max_level2_score:
        user.max_level2_score = level2_score
        user.save()
    if level3_score > user.max_level3_score:
        user.max_level3_score = level3_score
        user.save()
    if level4_score > user.max_level4_score:
        user.max_level4_score = level4_score
        user.save()

    return jsonify({"msg": "Game created successfully."}), 201
