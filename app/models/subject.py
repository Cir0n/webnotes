from app.config import Database

class SubjectModel:
    def __init__(self):
        self.db = Database()

    def add_subject(self, name):
        query = "INSERT INTO subject (name) VALUES (%s)"
        self.db.execute(query, (name,))

    def get_all_subjects(self):
        sql = "SELECT * FROM subjects"
        return self.db.query(sql)
    
    