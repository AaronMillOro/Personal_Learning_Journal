import datetime

from flask_bcrypt import generate_password_hash
from flask_login import UserMixin
from peewee import *

DATABASE = SqliteDatabase('learn_journal.db')

class Entry(Model):
    """Peewee model class for entries"""
    title = CharField()
    date = DateTimeField(default=datetime.datetime.now)
    timespent = IntegerField()
    learned = TextField()
    resources = TextField()

    class Meta:
        database = DATABASE

    def get_entry(self):
        return Entry.select().where(Entry.title == self)

    @classmethod
    def create_entry(cls, title, date, timespent, learned, resources):
        with DATABASE.transaction():
            cls.create(
                       title = title,
                       date = date,
                       timespent = timespent,
                       learned = learned,
                       resources = resources
                       )


def initialize():
    DATABASE.connect()
    DATABASE.create_tables([Entry], safe=True)
    DATABASE.close()
