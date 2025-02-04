from app.models.grade import GradeModel
from app.models.student import StudentModel
from app.models.teacher import TeacherModel
from app.models.user import UserModel


class TeacherController:
    def __init__(self):
        self.teacher_model = TeacherModel()
        self.user_model = UserModel()
        self.grade_model = GradeModel()
        self.student_model = StudentModel()

    def get_all_info_teacher(self, teacher_id):
        return self.teacher_model.get_all_info_teacher(teacher_id)

    def get_teacher(self, teacher_id):
        teacher = self.teacher_model.get_teacher_by_id(teacher_id)
        if not teacher:
            return "ERROR: Teacher not found"
        return teacher

    def list_teachers(self):
        return self.teacher_model.get_all_teachers()

    def edit_teacher(
        self,
        teacher_id,
        first_name,
        last_name,
        selected_classes,
        selected_languages,
        selected_options,
        selected_subjects,
    ):

        self.teacher_model.edit_teacher(
            teacher_id,
            first_name,
            last_name,
        )
        self.teacher_model.del_class_from_teacher(teacher_id)
        for class_id in selected_classes:
            self.teacher_model.edit_teacher_class_id(teacher_id, class_id)
        
        if selected_languages:
            self.teacher_model.edit_teacher_selected(
                teacher_id, selected_languages, selected_subjects, selected_options
            )

        return "Success: Teacher updated successfully"

    def create_teacher(
        self, username, password, first_name, last_name, class_ids, subject_ids
    ):
        user_id = self.user_model.add_user(username, password, role="teacher")
        self.teacher_model.create_teacher(
            user_id, first_name, last_name, class_ids, subject_ids
        )
        return "Success: Teacher created successfully"

    def delete_teacher(self, teacher_id):
        self.teacher_model.delete_teacher(teacher_id)

    def add_grade(self, teacher_id, student_id, subject_id, grade, comment=""):
        self.grade_model.add_grade(
            teacher_id, student_id, subject_id, grade, comment
        )

    def get_teacher_grades(self, teacher_id, student_id):
        return self.grade_model.get_student_grades(teacher_id, student_id)

    def get_teacher_classes(self, class_id):
        return self.teacher_model.get_teacher_classes(class_id)

    def get_subject_by_teacher(self, teacher_id):
        return self.teacher_model.get_subject_by_teacher(teacher_id)

    def delete_grade(self, teacher_id, grade_id):
        return self.grade_model.delete_grade(teacher_id, grade_id)
