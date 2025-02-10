from flask import (
    Blueprint,
    flash,
    redirect,
    render_template,
    session,
    url_for,
)

from app.controllers.student_controller import StudentController
from app.controllers.teacher_controller import TeacherController
from app.decorators import require_teacher
from app.forms.forms_add_grade import AddGradeForm
from app.forms.forms_delete_grade import DeleteGradeForm


class TeacherViews:
    def __init__(self):
        self.teacher_bp = Blueprint("teacher_bp", __name__)
        self.teacher_controller = TeacherController()
        self.student_controller = StudentController()
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
            classes = self.teacher_controller.get_teacher_classes(teacher_id)
            return render_template(
                "teacher/dashboard_teacher.html", classes=classes
            )

        @self.teacher_bp.route(
            "/class/<int:class_id>", methods=["GET", "POST"]
        )
        def class_students(class_id):
            teacher_id = session.get("user_id")

            student_class = self.student_controller.get_student_class(class_id)

            teacher_classes = self.teacher_controller.get_teacher_classes(
                teacher_id
            )
            subjects = self.teacher_controller.get_subject_by_teacher(
                teacher_id
            )

            form = AddGradeForm()
            form.subject_id.choices = [
                (subject["id"], subject["name"]) for subject in subjects
            ]

            if form.validate_on_submit():
                student_id = form.student_id.data
                subject_id = form.subject_id.data
                grade = form.grade.data
                comment = form.comment.data

                if not student_id or not student_id.isdigit():
                    flash("L'ID de l'étudiant est invalide.", "error")
                    return redirect(
                        url_for("teacher_bp.class_students", class_id=class_id)
                    )

                student_id = int(student_id)
                if not grade or not (0 <= float(grade) <= 20):
                    flash(
                        "La note doit être un nombre entre 0 et 20.", "error"
                    )
                    return redirect(
                        url_for("teacher_bp.class_students", class_id=class_id)
                    )

                self.teacher_controller.add_grade(
                    teacher_id, student_id, subject_id, grade, comment
                )

                flash("Note ajoutée avec succès !", "success")
                return redirect(
                    url_for("teacher_bp.class_students", class_id=class_id)
                )

            return render_template(
                "teacher/class_students.html",
                students=student_class,
                class_id=class_id,
                classes=teacher_classes,
                subjects=subjects,
                form=form,
            )

        @self.teacher_bp.route("/student/<int:student_id>")
        def student_grades(student_id):
            form = DeleteGradeForm()

            grades = self.student_controller.get_student_grades(student_id)
            student_info = self.student_controller.get_student_info(student_id)
            class_id = student_info["class_id"]

            return render_template(
                "teacher/student_grades.html",
                form=form,
                grades=grades,
                class_id=class_id,
                student_id=student_id,
            )

        @self.teacher_bp.route(
            "/delete_grade/<int:student_id>", methods=["POST"]
        )
        def delete_grade(student_id):
            teacher_id = session.get("user_id")

            form = DeleteGradeForm()

            if form.validate_on_submit():
                grade_id = form.grade_id.data
                self.teacher_controller.delete_grade(teacher_id, grade_id)

                flash("Note supprimée avec succès !")
            else:
                print("Erreur lors de la suppression de la note.", form.errors)

            return redirect(
                url_for("teacher_bp.student_grades", student_id=student_id)
            )
