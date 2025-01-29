from app.models.student import StudentModel
from app.models.user import UserModel


class StudentController:
    def __init__(self):
        self.model = StudentModel()
        self.user_model = UserModel()

    def get_student(self, student_id):
        student = self.model.get_student_by_id(student_id)
        if not student:
            return "ERROR: Student not found"
        return student

    def list_students(self):
        return self.model.get_all_students()

    def create_student(
        self, username, password, first_name, last_name, student_class):

        user_id = self.user_model.add_user(username, password, role="student")
        self.model.create_student(
            user_id, first_name, last_name, student_class
        )
        return "Success: Student created successfully"
