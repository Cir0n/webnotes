from functools import wraps

from flask import redirect, session, url_for

# Décorateurs pour la gestion des accès
def require_student(f):
    # Vérifie que l'utilisateur est un étudiant
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("role") != "student":
            return redirect(url_for("auth_bp.login"))
        return f(*args, **kwargs)

    return decorated_function

def require_teacher(f):
    # Vérifie que l'utilisateur est un professeur
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("role") != "teacher":
            return redirect(url_for("auth_bp.login"))
        return f(*args, **kwargs)

    return decorated_function

def require_admin(f):
    # Vérifie que l'utilisateur est un administrateur
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("role") != "admin":
            return redirect(url_for("auth_bp.login"))
        return f(*args, **kwargs)

    return decorated_function
