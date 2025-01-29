import os
from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from peewee import DoesNotExist
from models import User, KharazmiClass, db

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")
jwt = JWTManager(app)


@app.route("/signup", methods=["POST"])
def signup():
    username = request.json.get("username")
    password = request.json.get("password")
    class_name = request.json.get("class_name")

    if User.select().where(User.username == username).exists():
        return jsonify({"error": 1, "msg": "Username already exists!"}), 400

    if len(password) < 6:
        return jsonify({"error": 2, "msg": "Password is incorrect!"}), 400

    class_ref = (
        KharazmiClass.select().where(KharazmiClass.class_name == class_name).exists()
    )
    if not class_ref:
        return jsonify({"error": 3, "msg": "Class name was not exist!"}), 400

    user = User.create(username=username, password=password, class_ref=class_ref)
    return jsonify({"msg": "User created successfully."}), 201


@app.route("/login", methods=["POST"])
def login():
    username = request.json.get("username")
    password = request.json.get("password")

    try:
        user = User.get(User.username == username)
        if user.password != password:
            return jsonify({"error": 2, "msg": "Password is incorrect!"}), 401

    except DoesNotExist:
        return jsonify({"error": 1, "msg": "Username was not exist!"}), 401

    access_token = create_access_token(identity=user.username)
    return jsonify({"token": access_token, "msg": "Login was successful."}), 200


@app.route("/protected", methods=["GET"])
@jwt_required()
def protected():
    return jsonify({"msg": "This is a protected route"}), 200


if __name__ == "__main__":
    app.run(debug=True)
