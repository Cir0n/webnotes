from app.config import Database

class GradeModel:
    def __init__(self):
        self.db = Database()

    def add_grade(self, teacher_id, student_id, subject_id, grade, comment=""):
        # Check if subject_id exists in the subjects table
        subject_check_query = "SELECT id FROM subjects WHERE id = %s"
        subject_exists = self.db.query(subject_check_query, (subject_id,))
        if not subject_exists:
            raise ValueError("Invalid subject_id: Subject does not exist")

        query = "INSERT INTO grades (teacher_id, student_id, subject_id, grade, comment) VALUES (%s, %s, %s, %s, %s)"
        self.db.execute(query, (teacher_id, student_id, subject_id, grade, comment))

    def get_student_grades(self, teacher_id, student_id):
        query = """
        SELECT grades.grade, grades.comment, grades.created_at, sub.name AS subject_name
        FROM grades
        JOIN subjects sub ON grades.subject_id = sub.id
        WHERE grades.teacher_id = %s AND grades.student_id = %s
        ORDER BY grades.created_at DESC
        """
        return self.db.query(query, (teacher_id, student_id))