from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired


class DeleteTeacherForm(FlaskForm):
    teacher_id = StringField("teacher_id", validators=[InputRequired()])
    submit = SubmitField("Delete Teacher")
