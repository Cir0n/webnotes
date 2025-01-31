from flask import Blueprint, render_template, request, redirect, url_for, flash, session

from app.controllers.student_controller import StudentController
from app.controllers.subject_controller import SubjectController
from app.controllers.class_controller import ClassController
from app.controllers.teacher_controller import TeacherController



class AdminViews:
    def __init__(self):
        self.admin_bp = Blueprint("admin_bp", __name__)
        self.student_controller = StudentController()
        self.subject_controller = SubjectController()
        self.class_controller = ClassController()
        self.teacher_controller = TeacherController()
        self.register_routes()

    def require_admin(self):
        if session.get("role") != "admin":
            flash("You must be an admin to access this page")
            return redirect(url_for("auth_bp.login"))

    def register_routes(self):

        @self.admin_bp.route("/dashboard")
        def admin_dashboard():
            self.require_admin()
            return render_template("admin/dashboard.html")
        
        @self.admin_bp.route("/students")
        def list_students():
            self.require_admin()
            students = self.student_controller.list_students()
            options = self.subject_controller.get_options() 
            languages = self.subject_controller.get_languages() 
            return render_template("admin/students.html", students=students, options=[o['name'] for o in options], languages=[l['name'] for l in languages])

        
        @self.admin_bp.route("/add_student", methods=["GET", "POST"])
        def add_student():
            self.require_admin()
            classes = self.class_controller.get_all_classes()
            languages = self.subject_controller.get_languages()
            options = self.subject_controller.get_options()

            if request.method == "POST":
                username = request.form.get("username")
                password = request.form.get("password")
                first_name = request.form.get("first_name")
                last_name = request.form.get("last_name")
                class_id = request.form.get("class")
                selected_languages = request.form.getlist("languages")
                selected_options = request.form.getlist("options")

                result = self.student_controller.create_student(
                    username, password, first_name, last_name, class_id, selected_languages, selected_options
                )
                flash("etudiant ajouter avec succès")
                return redirect(url_for("admin_bp.list_students"))
            
            return render_template("admin/add_student.html", classes=classes, languages=languages, options=options)

        @self.admin_bp.route("/delete_student/<student_id>", methods=["POST"])
        def delete_student(student_id):
            self.require_admin()
            result = self.student_controller.delete_student(student_id)
            flash("Etudiant supprimé avec succès")
            return redirect(url_for("admin_bp.list_students"))
        
        #----------------------------TEACHERS--------------------------------

        @self.admin_bp.route("/teachers")
        def list_teachers():
            self.require_admin()
            teachers = self.teacher_controller.list_teachers()
            return render_template("admin/teachers.html", teachers=teachers)
        
        @self.admin_bp.route("/add_teacher", methods=["GET", "POST"])
        def add_teacher():
            self.require_admin()
            subjects = self.subject_controller.get_all_subjects()
            classes = self.class_controller.get_all_classes()
            
            if request.method == "POST":
                username = request.form.get("username")
                password = request.form.get("password")
                first_name = request.form.get("first_name")
                last_name = request.form.get("last_name")
                selected_classes = request.form.getlist("classes")
                selected_subjects = request.form.getlist("subjects")
                result = self.teacher_controller.create_teacher(
                    username, password, first_name, last_name, selected_classes, selected_subjects
                )
                flash(result)
                return redirect(url_for("admin_bp.list_teachers"))
            
            return render_template("admin/add_teacher.html", subjects=subjects, classes=classes)
        
        @self.admin_bp.route("/delete_teacher/<teacher_id>", methods=["POST"])
        def delete_teacher(teacher_id):
            self.require_admin()
            result = self.teacher_controller.delete_teacher(teacher_id)
            flash("Enseignant supprimé avec succès")
            return redirect(url_for("admin_bp.list_teachers"))
        
