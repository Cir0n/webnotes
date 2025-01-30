from flask import Blueprint, render_template, session

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
        
        
