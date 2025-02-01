import os
from dotenv import load_dotenv
from flask import Flask
from flask_jwt_extended import JWTManager

load_dotenv()

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")
JWTManager(app)

import main.db

import main.handlers
