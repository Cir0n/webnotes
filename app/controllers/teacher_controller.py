from app.models.teacher import TeacherModel
from app.models.user import UserModel
from app.models.grade import GradeModel
from app.models.student import StudentModel


class TeacherController:
    def __init__(self):
        self.teacher_model = TeacherModel()
        self.user_model = UserModel()
        self.grade_model = GradeModel()
        self.student_model = StudentModel()
    
    def get_teacher(self, teacher_id):
        teacher = self.teacher_model.get_teacher_by_id(teacher_id)
        if not teacher:
            return "ERROR: Teacher not found"
        return teacher
    
    def list_teachers(self):
        return self.teacher_model.get_all_teachers()
    
    def create_teacher(self, username, password, first_name, last_name, class_ids, subject_ids):
        user_id = self.user_model.add_user(username, password, role="teacher")
        self.teacher_model.create_teacher(user_id, first_name, last_name, class_ids, subject_ids)
        return "Success: Teacher created successfully"
    
    def delete_teacher(self, teacher_id):
        self.teacher_model.delete_teacher(teacher_id)

    def add_grade(self, teacher_id, student_id, subject_id, grade, comment=""):
        self.grade_model.add_grade(teacher_id, student_id, subject_id, grade, comment)

    def get_student_grades(self, teacher_id, student_id):
        return self.grade_model.get_student_grades(teacher_id, student_id)

    def get_student_classes(self, class_id):
        return self.student_model.get_student_classes(class_id)
    
    def get_teacher_classes(self, teacher_id):
        return self.teacher_model.get_teacher_classes(teacher_id)
    
    def get_teacher_subjects(self, teacher_id):
        return self.teacher_model.get_teacher_by_subject(teacher_id)

    def delete_grade(self, teacher_id, grade_id):
        return self.grade_model.delete_grade(teacher_id, grade_id)