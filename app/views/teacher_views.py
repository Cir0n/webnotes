from flask import Blueprint, render_template, session, request

from app.controllers.teacher_controller import TeacherController

class TeacherViews:
    def __init__(self):
        self.teacher_bp = Blueprint("teacher_bp", __name__)
        self.controller = TeacherController()
        self.register_route()

    def register_route(self):
        @self.teacher_bp.route("/me")
        def teacher_details():
            teacher_id = session.get("user_id")
            teacher = self.controller.get_teacher(teacher_id)
            if "error" in teacher:
                return render_template("error.html")
            return render_template("teacher/dashboard.html", teacher=teacher)
        
        @self.teacher_bp.route("/list")
        def list_teachers():
            teachers = self.controller.list_teachers()
            return render_template("teacher/list.html", teachers=teachers)
        
        @self.teacher_bp.route("/add_grade", methods=["POST"])
        def add_grade():
            teacher_id = session.get("user_id")
            student_id = request.form["student_id"]
            subject_id = request.form["subject_id"]
            grade = request.form["grade"]
            comment = request.form["comment"]

            self.controller.add_grade(teacher_id, student_id, subject_id, grade, comment)

        @self.teacher_bp.route("/student/<int:student_id>")
        def student_grades(student_id):
            teacher_id = session.get("user_id")
            grades = self.controller.get_student_grades(teacher_id, student_id)
            return render_template("teacher/student_grades.html", grades=grades)

        
