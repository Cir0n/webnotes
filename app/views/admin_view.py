from flask import (
    Blueprint,
    flash,
    redirect,
    render_template,
    request,
    session,
    url_for,
)

from app.controllers.class_controller import ClassController
from app.controllers.student_controller import StudentController
from app.controllers.subject_controller import SubjectController
from app.controllers.teacher_controller import TeacherController
from app.forms.forms_add_student import AddStudentForm
from app.forms.forms_add_teacher import AddTeacherForm
from app.forms.forms_delete_student import DeleteStudentForm
from app.forms.forms_delete_teacher import DeleteTeacherForm
from app.forms.forms_edit_student import EditStudentForm
from app.forms.forms_edit_teacher import EditTeacherForm


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
            form = DeleteStudentForm()
            students = self.student_controller.list_students()
            options = self.subject_controller.get_options()
            languages = self.subject_controller.get_languages()
            return render_template(
                "admin/students.html",
                form=form,
                students=students,
                options=[option["name"] for option in options],
                languages=[language["name"] for language in languages],
            )

        @self.admin_bp.route("/add_student", methods=["GET", "POST"])
        def add_student_form():
            self.require_admin()

            form = AddStudentForm()

            classes = self.class_controller.get_all_classes()
            languages = self.subject_controller.get_languages()
            options = self.subject_controller.get_options()

            form.class_id.choices = [
                (class_["id"], class_["name"]) for class_ in classes
            ]
            form.languages.choices = [
                (language["id"], language["name"]) for language in languages
            ]
            form.options.choices = [
                (option["id"], option["name"]) for option in options
            ]

            if request.method == "POST" and form.validate_on_submit():
                username = form.username.data
                password = form.password.data
                first_name = form.first_name.data
                last_name = form.last_name.data
                class_id = form.class_id.data
                selected_languages = form.languages.data
                selected_options = form.options.data

                self.student_controller.create_student(
                    username,
                    password,
                    first_name,
                    last_name,
                    class_id,
                    selected_languages,
                    selected_options,
                )

                flash("Étudiant ajouté avec succès", "success")
                return redirect(url_for("admin_bp.list_students"))

            return render_template(
                "admin/add_student.html",
                form=form,
                classes=classes,
                languages=languages,
                options=options,
            )

        @self.admin_bp.route(
            "/edit_student/<student_id>", methods=["GET", "POST"]
        )
        def edit_student(student_id):
            self.require_admin()

            student = self.student_controller.get_student_info(student_id)
            infos_student = self.student_controller.get_all_info_student(
                student_id
            )
            classes = self.class_controller.get_all_classes()
            languages = self.subject_controller.get_languages()
            options = self.subject_controller.get_options()

            if not student:
                flash("Étudiant non trouvé", "error")
                return redirect(url_for("admin_bp.list_students"))

            form = EditStudentForm()

            form.class_id.choices = [
                (class_["id"], class_["name"]) for class_ in classes
            ]
            form.languages.choices = [
                (lang["id"], lang["name"]) for lang in languages
            ]
            form.options.choices = [
                (opt["id"], opt["name"]) for opt in options
            ]

            if request.method == "POST" and form.validate_on_submit():
                self.student_controller.edit_student(
                    student_id,
                    form.first_name.data,
                    form.last_name.data,
                    form.class_id.data,
                    form.languages.data,
                    form.options.data,
                )
                flash("Étudiant modifié avec succès", "success")
                return redirect(url_for("admin_bp.list_students"))

            student = infos_student[0]
            student_subject_ids = [
                int(i) for i in student["subject_ids"].split(",")
            ]

            form.first_name.data = student["first_name"]
            form.last_name.data = student["last_name"]
            form.class_id.data = student["class_id"]
            form.languages.data = list(student_subject_ids)
            form.options.data = list(student_subject_ids)

            return render_template(
                "admin/edit_student.html",
                form=form,
                student=student,
                languages=languages,
                options=options,
            )

        @self.admin_bp.route("/delete_student/<student_id>", methods=["POST"])
        def delete_student(student_id):
            self.require_admin()
            form = DeleteStudentForm()

            if form.validate_on_submit():
                self.student_controller.delete_student(student_id)
                flash("Etudiant supprimé avec succès")
            else:
                print("Validation échouée :", form.errors)
            return redirect(url_for("admin_bp.list_students"))

        # ----------------------------TEACHERS--------------------------------

        @self.admin_bp.route("/teachers")
        def list_teachers():
            self.require_admin()
            form = DeleteTeacherForm()
            teachers = self.teacher_controller.list_teachers()
            return render_template(
                "admin/teachers.html", teachers=teachers, form=form
            )

        @self.admin_bp.route("/add_teacher", methods=["GET", "POST"])
        def add_teacher():
            self.require_admin()

            form = AddTeacherForm()

            subjects = self.subject_controller.get_all_subjects()
            classes = self.class_controller.get_all_classes()

            form.classes.choices = [
                (class_["id"], class_["name"]) for class_ in classes
            ]
            form.subjects.choices = [
                (subject["id"], subject["name"]) for subject in subjects
            ]

            if form.validate_on_submit():
                username = form.username.data
                password = form.password.data
                first_name = form.first_name.data
                last_name = form.last_name.data
                selected_classes = form.classes.data
                selected_subjects = form.subjects.data

                result = self.teacher_controller.create_teacher(
                    username,
                    password,
                    first_name,
                    last_name,
                    selected_classes,
                    selected_subjects,
                )

                flash(result)
                return redirect(url_for("admin_bp.list_teachers"))

            return render_template(
                "admin/add_teacher.html",
                form=form,
                subjects=subjects,
                classes=classes,
            )

        @self.admin_bp.route(
            "/edit_teacher/<teacher_id>", methods=["GET", "POST"]
        )
        def edit_teacher(teacher_id):
            self.require_admin()

            teacher = self.teacher_controller.get_teacher(teacher_id)
            infos_teacher = self.teacher_controller.get_all_info_teacher(
                teacher_id
            )

            if not teacher:
                flash("Enseignant non trouvé", "error")
                return redirect(url_for("admin_bp.list_teachers"))

            classes = self.class_controller.get_all_classes()
            languages = self.subject_controller.get_languages()
            options = self.subject_controller.get_options()
            subjects = self.subject_controller.get_subjects()

            form = EditTeacherForm()

            form.classes.choices = [
                (class_["id"], class_["name"]) for class_ in classes
            ]
            form.languages.choices = [
                (lang["id"], lang["name"]) for lang in languages
            ]
            form.options.choices = [
                (opt["id"], opt["name"]) for opt in options
            ]
            form.subjects.choices = [
                (subject["id"], subject["name"]) for subject in subjects
            ]

            if form.validate_on_submit():
                self.teacher_controller.edit_teacher(
                    teacher_id,
                    form.first_name.data,
                    form.last_name.data,
                    form.classes.data,
                    form.languages.data,
                    form.options.data,
                    form.subjects.data,
                )
                flash("Enseignant modifié avec succès", "success")
                return redirect(url_for("admin_bp.list_teachers"))

            teacher = infos_teacher[0]
            teacher_class_ids = [
                int(i) for i in teacher["class_ids"].split(",")
            ]
            teacher_subject_ids = [
                int(i) for i in teacher["subject_ids"].split(",")
            ]

            form.first_name.data = teacher["first_name"]
            form.last_name.data = teacher["last_name"]
            form.classes.data = teacher_class_ids
            form.languages.data = teacher_subject_ids
            form.options.data = teacher_subject_ids
            form.subjects.data = teacher_subject_ids

            return render_template(
                "admin/edit_teacher.html",
                form=form,
                teacher=teacher,
                classes=classes,
                languages=languages,
                options=options,
                subjects=subjects,
                teacher_class_ids=teacher_class_ids,
                teacher_subject_ids=teacher_subject_ids,
            )

        @self.admin_bp.route("/delete_teacher/<teacher_id>", methods=["POST"])
        def delete_teacher(teacher_id):
            self.require_admin()
            form = DeleteTeacherForm()

            if form.validate_on_submit():
                self.teacher_controller.delete_teacher(teacher_id)
                flash("Enseignant supprimé avec succès")
            else:
                print("Validation échouée :", form.errors)
            return redirect(url_for("admin_bp.list_teachers"))
