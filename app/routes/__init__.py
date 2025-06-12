# 각 route에서 블루프린트를 만들어주세요
# stats_routes_blp를 참고해주시면 됩니다!
from .answers import answers_blp
from .choices import choices_blp
from .questions import questions_blp
from .stats_routes import stats_routes_blp
from .users import user_blp
from .images import images_blp

def register_routes(application):
    # 코드를 작성해주세요
    application.register_blueprint(answers_blp)
    application.register_blueprint(choices_blp)
    application.register_blueprint(questions_blp)
    application.register_blueprint(stats_routes_blp)
    application.register_blueprint(user_blp)
    application.register_blueprint(images_blp)