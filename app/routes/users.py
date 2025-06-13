from flask import Blueprint, jsonify, request
from sqlalchemy.exc import IntegrityError

from app.models import User
from config import db

user_blp = Blueprint("users", __name__)


@user_blp.route("/", methods=["GET"])
def connect():
    if request.method == "GET":
        return jsonify({"message": "Success Connect"})


