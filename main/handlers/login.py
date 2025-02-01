from peewee import DoesNotExist
from flask import jsonify, request
from flask_jwt_extended import create_access_token

from main.db.models.User import User
from main import app


@app.route("/login", methods=["POST"])
def login():
    username = request.json.get("username")
    password = request.json.get("password")

    if not username:
        return jsonify({"error": 1, "msg": "Username cannot be empty!"}), 400

    if not password:
        return jsonify({"error": 2, "msg": "Password cannot be empty!"}), 400

    try:
        user = User.get(User.username == username)
        if user.password != password:
            return jsonify({"error": 4, "msg": "Password is incorrect!"}), 401

    except DoesNotExist:
        return jsonify({"error": 3, "msg": "Username was not exist!"}), 401

    access_token = create_access_token(identity=user.username)

    return jsonify({"token": access_token, "msg": "Login was successfully."}), 200
