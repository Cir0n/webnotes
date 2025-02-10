from app.config import Database


# Modèle pour gérer les données des professeurs
class TeacherModel:
    # Initialise la connexion à la base de données
    def __init__(self):
        self.db = Database()

    # Crée un nouveau professeur avec ses classes et matières
    def create_teacher(
        self, user_id, first_name, last_name, class_ids, subject_ids
    ):
        query = """INSERT INTO teachers ( id, first_name, last_name)
        VALUES (%s, %s, %s)"""
        self.db.execute(query, (user_id, first_name, last_name))

        if class_ids:
            for class_id in class_ids:
                query = """INSERT INTO teacher_class (teacher_id, class_id)
                VALUES (%s, %s)"""
                self.db.execute(query, (user_id, class_id))

        if subject_ids:
            for subject_id in subject_ids:
                query = """INSERT INTO teacher_subject (teacher_id, subject_id)
                VALUES (%s, %s)"""
                self.db.execute(query, (user_id, subject_id))
        return user_id

    # Modifie les informations de base d'un professeur
    def edit_teacher(
        self,
        teacher_id,
        first_name,
        last_name,
    ):
        query = (
            "UPDATE teachers SET first_name = %s, last_name = %s WHERE id = %s"
        )
        self.db.execute(query, (first_name, last_name, teacher_id))

    # Supprime toutes les classes assignées à un professeur
    def del_class_from_teacher(self, teacher_id):
        query = "DELETE FROM teacher_class WHERE teacher_id = %s"
        self.db.execute(query, (teacher_id,))

    # Assigne une nouvelle classe à un professeur
    def edit_teacher_class_id(self, teacher_id, class_id):
        query = (
            "INSERT INTO teacher_class (teacher_id, class_id) VALUES (%s, %s)"
        )
        self.db.execute(query, (teacher_id, class_id))

    # Met à jour les matières enseignées par un professeur
    def edit_teacher_selected(
        self,
        teacher_id,
        selected_languages,
        selected_subjects,
        selected_options,
    ):
        query = "DELETE FROM teacher_subject WHERE teacher_id = %s"
        self.db.execute(query, (teacher_id,))
        query = """INSERT INTO teacher_subject (teacher_id, subject_id)
        VALUES (%s, %s)"""
        for language in selected_languages:
            self.db.execute(query, (teacher_id, language))
        for subject in selected_subjects:
            self.db.execute(query, (teacher_id, subject))
        for option in selected_options:
            self.db.execute(query, (teacher_id, option))

    # Récupère la liste de tous les professeurs avec leurs classes et matières
    def get_all_teachers(self):
        query = """
        SELECT t.id, t.first_name, t.last_name,
            GROUP_CONCAT(DISTINCT c.name SEPARATOR ', ') AS classes,
            GROUP_CONCAT(DISTINCT s.name SEPARATOR ', ') AS subjects
        FROM teachers t
        LEFT JOIN teacher_class tc ON t.id = tc.teacher_id
        LEFT JOIN class c ON tc.class_id = c.id
        LEFT JOIN teacher_subject ts ON t.id = ts.teacher_id
        LEFT JOIN subjects s ON ts.subject_id = s.id
        GROUP BY t.id
        """
        return self.db.query(query)

    # Récupère un professeur par son ID
    def get_teacher_by_id(self, teacher_id):
        query = "SELECT * FROM teachers WHERE id = %s"
        result = self.db.query(query, (teacher_id,))
        return result[0] if result else None

    # Récupère toutes les informations d'un professeur
    def get_all_info_teacher(self, teacher_id):
        query = """
        SELECT t.id, t.first_name, t.last_name,
            GROUP_CONCAT(DISTINCT c.id SEPARATOR ',') AS class_ids,
            GROUP_CONCAT(DISTINCT s.id SEPARATOR ',') AS subject_ids
        FROM teachers t
        LEFT JOIN teacher_class tc ON t.id = tc.teacher_id
        LEFT JOIN class c ON tc.class_id = c.id
        LEFT JOIN teacher_subject ts ON t.id = ts.teacher_id
        LEFT JOIN subjects s ON ts.subject_id = s.id
        WHERE t.id = %s
        GROUP BY t.id
        """
        return self.db.query(query, (teacher_id,))

    # Supprime un professeur
    def delete_teacher(self, teacher_id):
        query = "DELETE FROM users WHERE id = %s"
        self.db.execute(query, (teacher_id,))

    # Récupère les classes d'un professeur
    def get_teacher_classes(self, teacher_id):
        query = """
        SELECT c.id, c.name
        FROM class c
        JOIN teacher_class tc ON c.id = tc.class_id
        WHERE tc.teacher_id = %s
        """
        return self.db.query(query, (teacher_id,))

    # Récupère les matières enseignées par un professeur
    def get_subject_by_teacher(self, teacher_id):
        query = """
        SELECT s.id, s.name
        FROM subjects s
        JOIN teacher_subject ts ON s.id = ts.subject_id
        WHERE ts.teacher_id = %s
        """
        return self.db.query(query, (teacher_id,))
