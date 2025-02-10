from app.config import Database


# Modèle pour gérer les opérations CRUD sur la table 'class'
class ClassModel:
    # Initialise la connexion à la base de données
    def __init__(self):
        self.db = Database()

    # Ajoute une nouvelle classe dans la base de données
    def add_class(self, name):
        query = "INSERT INTO class (name) VALUES (%s)"
        self.db.execute(query, (name,))

    # Récupère toutes les classes de la base de données
    def get_all_class(self):
        sql = "SELECT * FROM class"
        return self.db.query(sql)

    # Récupère une classe spécifique par son ID
    def get_one_class(self, class_id):
        sql = "SELECT * FROM class WHERE id = %s"
        return self.db.query(sql, (class_id,))
