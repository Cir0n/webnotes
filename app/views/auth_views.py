from flask import (
    Blueprint,
    redirect,
    render_template,
    request,
    session,
    url_for,
)

from app.controllers.auth_controller import AuthController
from app.forms.forms_auth import LoginForm


# Gestion de l'authentification
class AuthViews:
    def __init__(self):
        # Initialisation du blueprint et du contrôleur
        self.auth_bp = Blueprint("auth_bp", __name__)
        self.controller = AuthController()
        self.register_routes()

    def register_routes(self):
        # Route de connexion
        @self.auth_bp.route("/login", methods=["GET", "POST"])
        def login():
            form = LoginForm()

            if request.method == "POST" and form.validate_on_submit():
                username = form.username.data
                password = form.password.data
                result = self.controller.login(username, password)

                if "error" in result:
                    return render_template(
                        "auth/login.html", form=form, message=result["error"]
                    )

                if result["role"] == "student":
                    return redirect(url_for("student_bp.student_dashboard"))
                if result["role"] == "teacher":
                    return redirect(url_for("teacher_bp.teacher_dashboard"))
                if result["role"] == "admin":
                    return redirect(url_for("admin_bp.admin_dashboard"))

                return redirect("/profile")

            return render_template("auth/login.html", form=form)

        # Route de déconnexion
        @self.auth_bp.route("/logout")
        def logout():
            self.controller.logout()
            return redirect(url_for("auth_bp.login"))

        # Route du profil
        @self.auth_bp.route("/profile")
        def profile():
            if "user_id" in session:
                return f"""User {session["user_id"]} is logged in
                as {session["role"]}"""
            return "No user logged in"
