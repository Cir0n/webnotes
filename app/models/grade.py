from app.config import Database

class GradeModel:
    def __init__(self):
        self.db = Database()

    def add_grade(self, teacher_id, student_id, subject_id, grade, comment=""):
        query = "INSERT INTO grades (teacher_id, student_id, subject_id, grade, comment) VALUES (%s, %s, %s, %s, %s)"
        self.db.execute(query, (teacher_id, student_id, subject_id, grade, comment))

    def get_student_grades(self, teacher_id, student_id):
        query = """
        SELECT g.grade, g.comment, g.date_added, sub.name AS subject_name
        FROM grades g
        JOIN subjects sub ON g.subject_id = sub.id
        WHERE g.teacher_id = %s AND g.student_id = %s
        ORDER BY g.date_added DESC
        """
        return self.db.query(query, (teacher_id, student_id))