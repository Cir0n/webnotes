from app.models.teacher import TeacherModel
from app.models.user import UserModel

class TeacherController:
    def __init__(self):
        self.model = TeacherModel()
        self.user_model = UserModel()

    def get_teacher(self, teacher_id):
        teacher = self.model.get_teacher_by_id(teacher_id)
        if not teacher:
            return "ERROR: Teacher not found"
        return teacher
    
    def list_teachers(self):
        return self.model.get_all_teachers()
    
    def create_teacher(self, username, password, first_name, last_name, class_ids, subject_ids):
        
        user_id = self.user_model.add_user(username, password, role="teacher")
        self.model.create_teacher(user_id, first_name, last_name, class_ids, subject_ids)
        return "Success: Teacher created successfully"
    
    def delete_teacher(self, teacher_id):
        self.model.delete_teacher(teacher_id)

    