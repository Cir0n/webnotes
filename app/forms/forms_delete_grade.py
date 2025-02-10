from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired


class DeleteGradeForm(FlaskForm):
    grade_id = StringField("Grade ID", validators=[InputRequired()])
    student_id = StringField("Student ID", validators=[InputRequired()])
    submit = SubmitField("Supprimer la note")
