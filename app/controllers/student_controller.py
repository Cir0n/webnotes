from app.models.user import UserModel
from app.models.student import StudentModel

class StudentController:
    def __init__(self):
        self.model = StudentModel()
        self.user_model = UserModel()
    
    def get_student(self, student_id):
        student = self.model.get_student_by_id(student_id)
        if not student:
            return ("ERROR: Student not found")
        return student
    
    def list_students(self):
        return self.model.get_all_students()
    
    def create_student(self, username, password,first_name, last_name, student_class):
        if self.user_model.get_user_by_username(username):
            return ("ERROR: Username already exists")
        
        #TODO: Hasher le mots de passe et le mttre dans la base de données et ajouter les détails du user
        self.model.create_student(first_name, last_name, student_class)
        return ("Success: Student created successfully")
    