from flask_wtf import FlaskForm
from wtforms import StringField, SelectMultipleField, SubmitField
from wtforms.validators import DataRequired, Length

class EditTeacherForm(FlaskForm):
    first_name = StringField('Prénom', validators=[DataRequired(), Length(min=2, max=50)])
    last_name = StringField('Nom', validators=[DataRequired(), Length(min=2, max=50)])

    classes = SelectMultipleField('Classes', choices=[], coerce=int)  # Plusieurs classes possibles
    subjects = SelectMultipleField('Matières', choices=[], coerce=int)
    languages = SelectMultipleField('Langues', choices=[], coerce=int)
    options = SelectMultipleField('Options', choices=[], coerce=int)

    submit = SubmitField('Mettre à jour')
