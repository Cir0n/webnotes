from app.config import Database


# Modèle pour gérer les matières
class SubjectModel:
    # Initialise la connexion à la base de données
    def __init__(self):
        self.db = Database()

    # Ajoute une nouvelle matière
    def add_subject(self, name):
        query = "INSERT INTO subject (name) VALUES (%s)"
        self.db.execute(query, (name,))

    # Récupère toutes les matières
    def get_all_subjects(self):
        sql = "SELECT * FROM subjects"
        return self.db.query(sql)

    # Récupère uniquement les matières principales
    def get_subjects(self):
        sql = """SELECT id, name FROM subjects WHERE type = 'principal'
        ORDER BY name ASC"""
        return self.db.query(sql)

    # Récupère uniquement les langues disponibles
    def get_languages(self):
        sql = """SELECT id, name FROM subjects WHERE type = 'language'
        ORDER BY name ASC"""
        return self.db.query(sql)

    # Récupère uniquement les options disponibles
    def get_options(self):
        sql = """SELECT id, name FROM subjects WHERE type = 'option'
        ORDER BY name ASC"""
        return self.db.query(sql)
