import re


# Fonctions utilitaires de validation
def is_valid_name(name):
    # Vérifie si le nom contient uniquement des lettres et espaces
    return bool(re.match(r"^[a-zA-Z ]+$", name))


def is_valid_username(username):
    # Vérifie si le nom d'utilisateur est alphanumérique
    return bool(re.match(r"^[a-zA-Z0-9]+$", username))


def is_valid_grade(grade):
    # Vérifie si la note est entre 0 et 20
    try:
        grade = float(grade)
        return 0 <= grade <= 20
    except ValueError:
        return False
