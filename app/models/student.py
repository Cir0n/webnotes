from app.config import Database


class StudentModel:
    def __init__(self):
        self.db = Database()

    def get_student_by_id(self, student_id):
        query = "SELECT * FROM students WHERE id = %s"
        result = self.db.query(query, (student_id,))
        return result[0] if result else None

    def get_all_students(self):
        query = "SELECT * FROM students"
        return self.db.query(query)

    def create_student(self, user_id, first_name, last_name, student_class):
        query = "INSERT INTO students ( id, first_name, last_name, class) VALUES (%s, %s, %s, %s)"
        self.db.execute(query, (user_id, first_name, last_name, student_class))

    def delete_student(self, student_id):
        query = "DELETE FROM students WHERE id = %s"
        self.db.execute(query, (student_id,))

