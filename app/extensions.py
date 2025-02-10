# Extensions Flask pour la sécurité
# Protection CSRF et hachage des mots de passe
from flask_bcrypt import Bcrypt
from flask_wtf.csrf import CSRFProtect

csrf = CSRFProtect()

bcrypt = Bcrypt()
