from flask_wtf import FlaskForm
from wtforms import (
    DecimalField,
    SelectField,
    StringField,
    SubmitField,
)
from wtforms.validators import DataRequired, NumberRange, Optional


class AddGradeForm(FlaskForm):
    student_id = StringField("Student ID", validators=[DataRequired()])
    class_id = StringField("Class ID", validators=[DataRequired()])
    subject_id = SelectField(
        "Subject", coerce=int, validators=[DataRequired()]
    )
    grade = DecimalField(
        "Grade",
        validators=[DataRequired(), NumberRange(min=0, max=20)],
        places=1,
    )
    comment = StringField("Comment", validators=[Optional()])
    submit = SubmitField("Add Grade")
