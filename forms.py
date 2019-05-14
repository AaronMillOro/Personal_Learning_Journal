from flask_wtf import FlaskForm
from wtforms import StringField, DateField, IntegerField, TextAreaField

from wtforms.validators import DataRequired


class EntryForm(FlaskForm):
    title = StringField('Title',validators=[DataRequired(),])
    date = DateField('Date (DD-MM-YYYY)',format='%d-%m-%Y',validators=[
                                                            DataRequired()
                                                            ])
    timespent = IntegerField('Time spent',validators=[DataRequired()])
    learned = TextAreaField('What I learned',validators=[DataRequired()])
    resources = TextAreaField('Resources to remember',validators=[
                                                        DataRequired()
                                                        ])
