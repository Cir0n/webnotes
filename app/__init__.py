from flask import Flask
from app.views.student_views import StudentViews

def create_app():
    app = Flask(__name__)
    app.secret_key = 'secret_key'       #TODO: Faire une clé secrete pour les fonction de chiffrement 

    student_views = StudentViews()
    app.register_blueprint(student_views.student_bp)

    return app