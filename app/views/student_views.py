from flask import Blueprint, abort, render_template, request, session
from flask_login import login_required

from app.controllers.class_controller import ClassController
from app.controllers.student_controller import StudentController
from app.decorators import require_student


class StudentViews:
    def __init__(self):
        self.student_bp = Blueprint("student_bp", __name__)
        self.studentController = StudentController()
        self.classController = ClassController()
        self.register_routes()

    def register_routes(self):
        @self.student_bp.route("/me")
        def student_dashboard():
            student_id = session.get("user_id")
            if not student_id:
                return abort(401)  # Unauthorized

            student = self.studentController.get_student_info(student_id)
            if "error" in student:
                return render_template("error.html")

            class_student = []
            if hasattr(student, "get"):
                class_id = student.get("class_id")
                if class_id:
                    class_student = self.classController.get_one_class(
                        class_id
                    )
                    if not isinstance(class_student, list):
                        class_student = (
                            [class_student] if class_student else []
                        )

            return render_template(
                "student/dashboardStudent.html",
                student=student,
                class_=class_student,
            )

        @self.student_bp.route("/list")
        def list_students():
            students = self.studentController.list_students()
            return render_template("student/list.html", students=students)

        @self.student_bp.route("/add", methods=["GET", "POST"])
        def add_student():
            data = request.form
            self.studentController.create_student(
                first_name=data.get("first_name"),
                last_name=data.get("last_name"),
                student_class=data.get("class"),
            )
            return render_template("student/add.html")

        @self.student_bp.route("/mail")
        @require_student
        def student_mail():
            student_id = session.get("user_id")
            student = self.studentController.get_student_info(student_id)
            return render_template("student/mail.html", student=student)

        @self.student_bp.route("/presence")
        @login_required
        def presence():
            return render_template("student/presence.html")

        @self.student_bp.route("/homework")
        @require_student
        def student_homework():
            student_id = session.get("user_id")
            student = self.studentController.get_student_info(student_id)
            return render_template("student/homework.html", student=student)

        @self.student_bp.route("/schedule")
        @require_student
        def student_schedule():
            student_id = session.get("user_id")
            student = self.studentController.get_student_info(student_id)
            class_student = (
                self.classController.get_one_class(student["class_id"])
                if student.get("class_id")
                else None
            )
            return render_template(
                "student/schedule.html", student=student, class_=class_student
            )

        @self.student_bp.route("/grades")
        @require_student
        def student_grades():
            student_id = session.get("user_id")
            student = self.studentController.get_student_info(student_id)
            class_student = (
                self.classController.get_one_class(student["class_id"])
                if student.get("class_id")
                else None
            )
            return render_template(
                "student/grades.html", student=student, class_=class_student
            )
