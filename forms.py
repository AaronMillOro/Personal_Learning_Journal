from flask_wtf import Form
from wtforms import StringField, DateField, IntegerField, TextAreaField
from wtforms.validators import DataRequired, ValidationError, Length
"""
Information about wtforms fields obtained from:
https://wtforms.readthedocs.io/en/stable/fields.html
"""

from models import Entry


class EntryForm(Form):
    title = StringField(
        'Title',
        validators=[
            DataRequired(),
            Length(min=3, message='Use at least 3 characters')
            ])
    date = DateField(
        'Date (DD-MM-YYYY)',
        format='%d-%m-%Y',
        validators=[
            DataRequired()
            ])
    timespent = IntegerField(
        'Time spent',
        validators=[
            DataRequired(),
            Length(min=1)
            ])
    learned = TextAreaField(
        'What I learned',
        validators=[
            DataRequired()
            ])
    resources = TextAreaField(
        'Resources to Remember',
        validators=[
            DataRequired()
            ])
