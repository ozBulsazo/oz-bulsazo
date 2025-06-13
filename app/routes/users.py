from flask import Blueprint, jsonify, request
from sqlalchemy.exc import IntegrityError

from app.models import User  # SQLAlchemy 모델
from config import db        # SQLAlchemy 인스턴스

user_blp = Blueprint('user', __name__, url_prefix='/')

@user_blp.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()

    # 필수 필드 체크
    if not data:
        return jsonify({"message": "요청 본문이 없습니다."}), 400

    if not all(k in data for k in ("name", "email", "age", "gender")):
        return jsonify({"message": "필수 필드가 누락되었습니다 (name, email, age, gender)."}), 400

    name = data.get("name")
    email = data.get("email")
    age = data.get("age")
    gender = data.get("gender")

    # 유효성 검사 예시 (필요 시 확장 가능)
    if not isinstance(age, int) or not (0 < age < 120):
        return jsonify({"message": "유효하지 않은 age 값입니다."}), 400

    if gender not in ['male', 'female']:
        return jsonify({"message": "유효하지 않은 gender 값입니다."}), 400

    # 사용자 생성
    new_user = User(name=name, email=email, age=age, gender=gender)

    try:
        db.session.add(new_user)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return jsonify({"message": "이미 존재하는 계정 입니다."}), 409

    return jsonify({
        "message": f"{name}님 회원가입을 축하합니다!",
        "user_id": new_user.id
    }), 200
