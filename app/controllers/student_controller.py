from app.models.student import StudentModel
from app.models.grade import GradeModel
from app.models.user import UserModel
from app.utils import is_valid_name, is_valid_username, is_valid_grade


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

    def get_all_info_student(self, student_id):
        return self.model.get_all_info_student(student_id)

    def edit_student(
        self,
        student_id,
        first_name,
        last_name,
        class_id,
        selected_languages,
        selected_options,
    ):

        self.model.edit_student(
            student_id,
            first_name,
            last_name,
            class_id,
            selected_languages,
            selected_options,
        )
        return "Success: Student updated successfully"

    def list_students(self):
        return self.model.get_all_students()

    def get_student_class(self, student_id):
        return self.model.get_student_class(student_id)

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
        if not is_valid_name(first_name):
            return {"error": "Le prenom doit contenir que des lettres"}
        
        if not is_valid_username(username):
            return {"error": "Le nom d'utilisateur doit contenir que des lettre, chiffre et underscores."}
        
        if self.user_model.get_user_by_username(username):
            return {"error": "Le nom d'utilisateur est déjà utilisé"}

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