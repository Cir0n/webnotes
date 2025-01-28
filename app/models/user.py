from app.config import Database

class UserModel:
    def __init__(self):
        self.db = Database()

    def add_user(self, username, password, role):
        sql = "INSERT INTO users (username, password, role) VALUES (%s, %s, %s)"
        self.db.execute(sql, (username, password, role))
        return self.db.cursor.lastrowid  # Retourne l'ID de l'utilisateur ajouté

    def get_user_by_username(self, username):
        sql = "SELECT * FROM users WHERE username = %s"
        result = self.db.query(sql, (username,))
        return result[0] if result else None
