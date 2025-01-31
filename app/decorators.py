from flask import session, render_template
from functools import wraps

def require_teacher(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        role = session.get("role")
        if role not in ["teacher", "admin"]:
            return render_template("errors/unauthorized.html", role=role)
        return f(*args, **kwargs)
    return decorated_function
