from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectMultipleField, RadioField, SubmitField
from wtforms.validators import DataRequired, Length

class AddStudentForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=50)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    first_name = StringField('First Name', validators=[DataRequired(), Length(min=2, max=50)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(min=2, max=50)])
    class_id = RadioField('Class', coerce=int, choices=[]) 
    languages = SelectMultipleField('Languages', coerce=int, choices=[]) 
    options = SelectMultipleField('Options', coerce=int, choices=[])

    submit = SubmitField('Add Student')  
