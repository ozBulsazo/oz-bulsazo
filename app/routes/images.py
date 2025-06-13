from flask import jsonify, request, Blueprint
from app.models import Image
from config import db

images_blp = Blueprint("images", __name__)

@images_blp.route("/image", methods=["POST"])
def create_image():
    if request.method == "POST":
        try:
            data = request.get_json()
            image = Image(
                url=data["url"],
                type=data["type"],
            )
            db.session.add(image)
            db.session.commit()
            return jsonify({"message": f"ID: {image.id} Image Success Create"}), 201

        except KeyError as e:
            return jsonify({"message": f"Missing required field: {str(e)}"}), 400
