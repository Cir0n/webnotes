from app.config import Database


class GradeModel:
    def __init__(self):
        self.db = Database()

    def add_grade(self, teacher_id, student_id, subject_id, grade, comment=""):
        query = "INSERT INTO grades (teacher_id, student_id, subject_id, grade, comment) VALUES (%s, %s, %s, %s, %s)"
        return self.db.execute(
            query, (teacher_id, student_id, subject_id, grade, comment)
        )

    def get_student_grades(self, teacher_id, student_id):
        query = """
        SELECT g.id, g.grade, g.comment, g.created_at AS date_added, sub.name AS subject_name
        FROM grades g
        JOIN subjects sub ON g.subject_id = sub.id
        WHERE g.teacher_id = %s AND g.student_id = %s
        ORDER BY g.created_at DESC
        """
        return self.db.query(query, (teacher_id, student_id))

    def delete_grade(self, teacher_id, grade_id):
        query = "DELETE FROM grades WHERE teacher_id = %s AND id = %s"
        return self.db.execute(query, (teacher_id, grade_id))
