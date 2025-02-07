from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectMultipleField, SubmitField
from wtforms.validators import DataRequired, Length

class AddTeacherForm(FlaskForm):
    username = StringField('Nom d’utilisateur', validators=[DataRequired(), Length(min=4, max=50)])
    password = PasswordField('Mot de passe', validators=[DataRequired(), Length(min=6)])
    first_name = StringField('Prénom', validators=[DataRequired(), Length(min=2, max=50)])
    last_name = StringField('Nom', validators=[DataRequired(), Length(min=2, max=50)])

    classes = SelectMultipleField('Classes',choices=[], coerce=int)
    subjects = SelectMultipleField('Matières',choices=[] ,coerce=int)

    submit = SubmitField('Ajouter un professeur')
