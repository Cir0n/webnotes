from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, SelectMultipleField, SubmitField
from wtforms.validators import DataRequired

class EditStudentForm(FlaskForm):
    first_name = StringField("Prénom", validators=[DataRequired()])
    last_name = StringField("Nom", validators=[DataRequired()])
    
    class_id = RadioField("Classe", choices=[], coerce=int, validators=[DataRequired()])
    
    languages = SelectMultipleField("Langues", choices=[], coerce=int)
    options = SelectMultipleField("Options", choices=[], coerce=int)
    
    submit = SubmitField("Mettre à jour")
