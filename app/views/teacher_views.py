from flask import Blueprint, render_template, session, request, flash

from app.controllers.teacher_controller import TeacherController
from app.decorators import require_teacher

class TeacherViews:
    def __init__(self):
        self.teacher_bp = Blueprint("teacher_bp", __name__)
        self.controller = TeacherController()
        self.register_route()

    def require_teacher(self):
        if session.get("role") not in ["teacher", "admin"]:
            flash("You must be a teacher to access this page")
            return render_template("errors/unauthorized.html")
        return None

    def register_route(self):
        
        @self.teacher_bp.route("/dashboard")
        @require_teacher
        def teacher_dashboard():        
            teacher_id = session.get("user_id")
            classes = self.controller.get_teacher_classes(teacher_id)
            return render_template("teacher/dashboard.html", classes=classes)
        
        @self.teacher_bp.route("/class/<int:class_id>")
        def class_students(self, class_id):
            teacher_id = session.get("user_id")
            students = self.controller.get_student_classes(class_id)
            return render_template("teacher/class_students.html", students=students, class_id=class_id)
        

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

        
