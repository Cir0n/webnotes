from app.config import Database


class TeacherModel:
    def __init__(self):
        self.db = Database()

    def get_teacher_by_id(self, teacher_id):
        query = "SELECT * FROM teachers WHERE id = %s"
        result = self.db.query(query, (teacher_id,))
        return result[0] if result else None

    def get_all_teachers(self):
        query = "SELECT * FROM teachers"
        return self.db.query(query)

    def create_teacher(self, user_id, first_name, last_name, matiere):
        query = "INSERT INTO teachers ( id, first_name, last_name, matiere) VALUES (%s, %s, %s, %s)"
        self.db.execute(query, (user_id, first_name, last_name, matiere))

    def delete_teacher(self, teacher_id):
        query = "DELETE FROM teachers WHERE id = %s"
        self.db.execute(query, (teacher_id,))
    