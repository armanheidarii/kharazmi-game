from flask import jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from main.db.enums.GameLevel import GameLevel
from main import app


@app.route("/game", methods=["POST"])
@jwt_required()
def game():
    current_user = get_jwt_identity()

    game_level = request.json.get("game_level")
    level1_score = request.json.get("level1_score")
    level2_score = request.json.get("level2_score")
    level3_score = request.json.get("level3_score")
    level4_score = request.json.get("level4_score")

    if game_level not in GameLevel:
        return jsonify({"error": 1, "msg": "Game level is invalid!"}), 400

    final_score = level1_score + level2_score + level3_score + level4_score

    game = Game.create(
        game_level=game_level,
        level1_score=level1_score,
        level2_score=level2_score,
        level3_score=level3_score,
        level4_score=level4_score,
        final_score=final_score,
    )

    return jsonify({"msg": "Game created successfully."}), 201
