from peewee import DoesNotExist
from flask import jsonify, request

from main.db.models.User import User
from main.db.models.KharazmiClass import KharazmiClass
from main import app


@app.route("/signup", methods=["POST"])
def signup():
    username = request.json.get("username")
    password = request.json.get("password")
    email = request.json.get("email")
    class_name = request.json.get("class_name")

    if not username:
        return jsonify({"error": 1, "msg": "Username cannot be empty!"}), 400

    if not password:
        return jsonify({"error": 2, "msg": "Password cannot be empty!"}), 400

    if not class_name:
        return jsonify({"error": 3, "msg": "Class name cannot be empty!"}), 400

    try:
        User.get(User.username == username)
        return jsonify({"error": 4, "msg": "Username already exists!"}), 400

    except DoesNotExist:
        pass

    if len(password) < 6:
        return jsonify({"error": 5, "msg": "Password is incorrect!"}), 400

    if email and not validators_email(email):
        return jsonify({"error": 6, "msg": "Email is invalid!"}), 400

    class_ref = (
        KharazmiClass.select().where(KharazmiClass.class_name == class_name).exists()
    )
    if not class_ref:
        return jsonify({"error": 7, "msg": "Class name was not exist!"}), 400

    user = User.create(
        username=username,
        password=password,
        email=email,
        class_ref=class_ref,
    )

    return jsonify({"msg": "User created successfully."}), 201
