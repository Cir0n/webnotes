from flask import (
    Blueprint,
    redirect,
    render_template,
    request,
    session,
    url_for,
)

from app.controllers.auth_controller import AuthController


class AuthViews:
    def __init__(self):
        self.auth_bp = Blueprint("auth_bp", __name__)
        self.controller = AuthController()
        self.register_routes()

    def register_routes(self):

        @self.auth_bp.route("/login", methods=["GET", "POST"])
        def login():
            if request.method == "POST":
                username = request.form.get("username")
                password = request.form.get("password")
                result = self.controller.login(username, password)

                if "error" in result:
                    return render_template(
                        "auth/login.html", message=result["error"]
                    )
                if result["role"] == "student":
                    return redirect(url_for("student_bp.student_details"))
                if result["role"] == "teacher":
                    return redirect(url_for("teacher_bp.teacher_details")) #FIXME: teacher_bp is not defined mais marche pour student
                if result["role"] == "admin":
                    return redirect(url_for("admin_bp.admin_dashboard"))
            
                return redirect("/profile")
            return render_template("auth/login.html")

        @self.auth_bp.route("/register", methods=["GET", "POST"])
        def register():
            if request.method == "POST":
                username = request.form.get("username")
                password = request.form.get("password")
                role = request.form.get("role")
                first_name = request.form.get("first_name")
                last_name = request.form.get("last_name")
                additional_info = request.form.get("additional_info")

                result = self.controller.register(
                    username,
                    password,
                    role,
                    first_name,
                    last_name,
                    additional_info,
                )

                if "error" in result:
                    return render_template(
                        "auth/register.html", message=result["error"]
                    )

                return redirect(url_for("auth_bp.login"))

            return render_template("auth/register.html")

        @self.auth_bp.route("/logout")
        def logout():
            self.controller.logout()
            return redirect(url_for("auth_bp.login"))

        @self.auth_bp.route("/profile")
        def profile():
            if "user_id" in session:
                return f"User {session['user_id']} is logged in as {session['role']}"
            return "No user logged in"
