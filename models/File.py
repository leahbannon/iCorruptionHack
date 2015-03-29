import re
from blessings import Terminal
from peewee import *

t = Terminal()
db = SqliteDatabase('contributions.db')

class File(Model):
    name = CharField(null=True, default=None)
    year = IntegerField(null=True, default=None)
    updated = DateTimeField(null=True, default=None)

    class Meta:
        database = db

    def __str__(self):
        return self.name


