import re
from blessings import Terminal
from peewee import *
from File import File

t = Terminal()
db = SqliteDatabase('contributions.db')

class Contribution(Model):
    comittee_id = CharField(null=True, default=None)
    ammendment_id = CharField(null=True, default=None)
    report_type = CharField(null=True, default=None)
    transaction_pgi = CharField(null=True, default=None)
    image_num = CharField(null=True, default=None)
    transaction_tp = CharField(null=True, default=None)
    entity_tp = CharField(null=True, default=None)
    name = CharField(null=True, default=None)
    city = CharField(null=True, default=None)
    state = CharField(null=True, default=None)
    zip_code = CharField(null=True, default=None)
    employer = CharField(null=True, default=None)
    occupation = CharField(null=True, default=None)
    transaction_date = DateTimeField(null=True, default=None)
    transaction_amount = FloatField(null=True, default=None)
    other_id = CharField(null=True, default=None)
    transaction_id = CharField(null=True, default=None)
    file_num = IntegerField(null=True, default=None)
    memo_cd = CharField(null=True, default=None)
    memo_text = CharField(null=True, default=None)
    sub_id = IntegerField(null=True, default=None)
    
    file = ForeignKeyField(File, null=True, default=None)

    class Meta:
        database = db
