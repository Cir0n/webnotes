from flask import Blueprint, render_template, request, session

from app.controllers.class_controller import ClassController
from app.controllers.student_controller import StudentController


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
            student = self.studentController.get_student_info(student_id)
            class_student = self.classController.get_one_class(
                student["class_id"]
            )
            if "error" in student:
                return render_template("error.html")
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
