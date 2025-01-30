from flask import Flask

from app.extensions import bcrypt
from app.views.auth_views import AuthViews
from app.views.student_views import StudentViews
from app.views.teacher_views import TeacherViews
from app.views.admin_view import AdminViews


def create_app():
    app = Flask(__name__)

    app.config["SECRET_KEY"] = (
        "your_secret_key"  # TODO: créer une clé secrête
    )

    bcrypt.init_app(app)

    student_views = StudentViews()
    teacher_views = TeacherViews()
    auth_views = AuthViews()
    admin_views = AdminViews()


    app.register_blueprint(student_views.student_bp, url_prefix="/students")
    app.register_blueprint(teacher_views.teacher_bp, url_prefix="/teachers")
    app.register_blueprint(auth_views.auth_bp, url_prefix="/")
    app.register_blueprint(admin_views.admin_bp, url_prefix="/admin")

    return app
