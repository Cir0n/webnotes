from functools import wraps

from flask import redirect, session, url_for


def require_student(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("role") != "student":
            return redirect(url_for("auth_bp.login"))
        return f(*args, **kwargs)

    return decorated_function


def require_teacher(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("role") != "teacher":
            return redirect(url_for("auth_bp.login"))
        return f(*args, **kwargs)

    return decorated_function


def require_admin(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("role") != "admin":
            return redirect(url_for("auth_bp.login"))
        return f(*args, **kwargs)

    return decorated_function
