from app.config import Database


# Modèle pour gérer les données des étudiants
class StudentModel:
    # Initialise la connexion à la base de données
    def __init__(self):
        self.db = Database()

    # Récupère un étudiant par son ID
    def get_student_by_id(self, student_id):
        query = """SELECT id, first_name, last_name, class_id FROM students
                    WHERE id = %s"""
        result = self.db.query(
            query, (student_id,)
        )  # Exécute la requête normalement
        return result[0] if result else None

    # Récupère tous les étudiants avec leurs classes et matières
    def get_all_students(self):
        sql = """
        SELECT s.id, s.first_name, s.last_name, c.name AS class_name,
            GROUP_CONCAT(DISTINCT sub.name SEPARATOR ', ') AS subjects
        FROM students s
        LEFT JOIN class c ON s.class_id = c.id
        LEFT JOIN student_subject ss ON s.id = ss.student_id
        LEFT JOIN subjects sub ON ss.subject_id = sub.id
        GROUP BY s.id, s.first_name, s.last_name, c.name
        """
        return self.db.query(sql)

    # Récupère toutes les informations d'un étudiant spécifique
    def get_all_info_student(self, student_id):
        query = """
        SELECT
        s.id,
        s.first_name,
        s.last_name,
        s.class_id AS class_id,  -- Un élève appartient à une seule classe
        GROUP_CONCAT(DISTINCT sub.id SEPARATOR ',') AS subject_ids
        FROM students s
        LEFT JOIN student_subject ss ON s.id = ss.student_id
        LEFT JOIN subjects sub ON ss.subject_id = sub.id
        WHERE s.id = %s
        GROUP BY s.id, s.first_name, s.last_name, s.class_id;
        """
        return self.db.query(query, (student_id,))

    # Modifie les informations d'un étudiant existant
    def edit_student(
        self,
        student_id,
        first_name,
        last_name,
        class_id,
        selected_languages,
        selected_options,
    ):
        query = """
            UPDATE students
            SET first_name = %s, last_name = %s, class_id = %s
            WHERE id = %s
        """
        self.db.execute(query, (first_name, last_name, class_id, student_id))

        query_delete = "DELETE FROM student_subject WHERE student_id = %s"
        self.db.execute(query_delete, (student_id,))

        sql_principal_subject = (
            "SELECT id FROM subjects WHERE type = 'Principal'"
        )
        principal_subjects = self.db.query(sql_principal_subject)

        query = """INSERT INTO student_subject (student_id, subject_id)
        VALUES (%s, %s)"""

        for subject in principal_subjects:
            self.db.execute(query, (student_id, subject["id"]))

        for language in selected_languages:
            self.db.execute(query, (student_id, language))

        for option in selected_options:
            self.db.execute(query, (student_id, option))

    # Crée un nouvel étudiant avec ses matières
    def create_student(
        self,
        user_id,
        first_name,
        last_name,
        class_id,
        selected_languages,
        selected_options,
    ):
        query = """INSERT INTO students ( id, first_name, last_name, class_id)
        VALUES (%s, %s, %s, %s)"""
        self.db.execute(query, (user_id, first_name, last_name, class_id))

        sql_principal_subject = (
            "Select id from subjects where type = 'Principal'"
        )
        principal_subjects = self.db.query(sql_principal_subject)

        for subject in principal_subjects:
            query = """INSERT INTO student_subject (student_id, subject_id)
                     VALUES (%s, %s)"""
            self.db.execute(query, (user_id, subject["id"]))

        query = """INSERT INTO student_subject (student_id, subject_id)
        VALUES (%s, %s)"""

        for language in selected_languages:
            self.db.execute(query, (user_id, language))

        for option in selected_options:
            self.db.execute(query, (user_id, option))

        return user_id

    # Récupère tous les étudiants d'une classe spécifique
    def get_student_class(self, class_id):
        query = """
        SELECT id, first_name, last_name
        From students
        WHERE class_id = %s
        """
        return self.db.query(query, (class_id,))

    # Supprime un étudiant
    def delete_student(self, student_id):
        query = "DELETE FROM users WHERE id = %s"
        self.db.execute(query, (student_id,))

    # Récupère toutes les matières d'un étudiant
    def get_student_subject(self, student_id):
        query = """
        SELECT s.id, s.name, s.type
        FROM subjects s
        JOIN student_subject ss ON s.id = ss.subject_id
        WHERE ss.student_id = %s
        """
        return self.db.query(query, (student_id,))

    # Récupère une matière par son ID
    def get_subject_by_id(self, subject_id):
        query = "SELECT id, name, type FROM subjects WHERE id = %s"
        result = self.db.query(query, (subject_id,))
        return result[0] if result else None
