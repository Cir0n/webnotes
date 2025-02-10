from app.config import Database


# Modèle pour gérer les notes et évaluations des élèves
class GradeModel:
    # Initialise la connexion à la base de données
    def __init__(self):
        self.db = Database()

    # Ajoute une nouvelle note pour un élève
    def add_grade(self, teacher_id, student_id, subject_id, grade, comment=""):
        query = """INSERT INTO grades (student_id, teacher_id, subject_id,
        grade, comment) VALUES (%s, %s, %s, %s, %s)"""
        self.db.execute(
            query, (student_id, teacher_id, subject_id, grade, comment)
        )

    # Récupère toutes les notes d'un élève pour un professeur donné
    def get_student_grades(self, teacher_id, student_id):
        query = """
        SELECT g.id, g.grade, g.comment, g.created_at AS date_added,
        sub.name AS subject_name
        FROM grades g
        JOIN subjects sub ON g.subject_id = sub.id
        WHERE g.teacher_id = %s AND g.student_id = %s
        ORDER BY g.created_at DESC
        """
        return self.db.query(query, (teacher_id, student_id))

    # Supprime une note spécifique
    def delete_grade(self, teacher_id, grade_id):
        query = "DELETE FROM grades WHERE teacher_id = %s AND id = %s"
        self.db.execute(query, (teacher_id, grade_id))

    # Récupère toutes les notes d'un élève avec détails des professeurs et matières
    def get_student_grade_by_student(self, student_id):
        query = """
        SELECT g.id, g.grade, g.comment, g.created_at AS date_added,
        sub.name AS subject_name, t.first_name AS teacher_name
        FROM grades g
        JOIN subjects sub ON g.subject_id = sub.id
        JOIN teachers t ON g.teacher_id = t.id
        WHERE g.student_id = %s
        ORDER BY g.created_at DESC
        """
        return self.db.query(query, (student_id,))

    # Récupère les notes d'un élève pour une matière spécifique
    def get_student_grades_by_subject(self, student_id, subject_id):
        query = """
        SELECT g.grade, g.comment, g.created_at AS date_added, sub.name
        AS subject_name, t.first_name AS teacher_name
        FROM grades g
        JOIN subjects sub ON g.subject_id = sub.id
        JOIN teachers t ON g.teacher_id = t.id
        WHERE g.student_id = %s AND g.subject_id = %s
        ORDER BY g.created_at DESC
        """
        return self.db.query(query, (student_id, subject_id))
