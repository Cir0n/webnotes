from flask import Flask

from app.extensions import bcrypt
from app.views.auth_views import AuthViews
from app.views.student_views import StudentViews


def create_app():
    app = Flask(__name__)

    app.config["SECRET_KEY"] = (
        "your_secret_key"  # TODO: créer une clé secrête
    )

    bcrypt.init_app(app)

    student_views = StudentViews()
    auth_views = AuthViews()

    app.register_blueprint(student_views.student_bp, url_prefix="/students")
    app.register_blueprint(auth_views.auth_bp, url_prefix="/")

    return app
