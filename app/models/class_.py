from app.config import Database


class ClassModel:
    def __init__(self):
        self.db = Database()

    def add_class(self, name):
        query = "INSERT INTO class (name) VALUES (%s)"
        self.db.execute(query, (name,))

    def get_all_class(self):
        sql = "SELECT * FROM class"
        return self.db.query(sql)
