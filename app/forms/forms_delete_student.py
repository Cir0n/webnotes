from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired

class DeleteStudentForm(FlaskForm):
    student_id = StringField('student_id', validators=[InputRequired()])
    submit = SubmitField('Delete Student')
