from flask import jsonify, request, Blueprint
from app.models import Image


images_blp = Blueprint("images", __name__)


@images_blp.route("/image/main", methods=["GET"])
def get_main_image_route():
    if request.method == "GET":
        main_image_url = "https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png"
        return jsonify({"image": main_image_url}), 200
