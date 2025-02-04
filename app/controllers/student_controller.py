from app.models.student import StudentModel
from app.models.grade import GradeModel
from app.models.user import UserModel


class StudentController:
    def __init__(self):
        self.model = StudentModel()
        self.user_model = UserModel()
        self.grade_model = GradeModel()

    def get_student_info(self, student_id):
        student = self.model.get_student_by_id(student_id)
        if not student:
            return "ERROR: Student not found"
        return student

    def list_students(self):
        return self.model.get_all_students()

    def create_student(
        self,
        username,
        password,
        first_name,
        last_name,
        class_id,
        selected_languages,
        selected_options,
    ):

        user_id = self.user_model.add_user(username, password, role="student")
        self.model.create_student(
            user_id,
            first_name,
            last_name,
            class_id,
            selected_languages,
            selected_options,
        )
        return "Success: Student created successfully"

    def delete_student(self, student_id):
        self.model.delete_student(student_id)

    def get_student_grades(self, student_id):
        grades = self.grade_model.get_student_grade_by_student(student_id)
        return grades if grades else []
    
    def get_student_subject(self, student_id):
        subjects = self.model.get_student_subject(student_id)
        return subjects if subjects else []

    def get_student_grades_by_subject(self, student_id, subject_id):
        grades = self.grade_model.get_student_grades_by_subject(student_id, subject_id)
        return grades if grades else []

    def get_subject_info(self, subject_id):
        subject = self.model.get_subject_by_id(subject_id)
        return subject 