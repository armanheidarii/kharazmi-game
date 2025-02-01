from peewee import IntegerField, CharField, ForeignKeyField

from main.db import db
from main.db.models.Base import BaseModel
from main.db.models.KharazmiClass import KharazmiClass


class User(BaseModel):
    username = CharField(unique=True)
    password = CharField()
    email = CharField(null=True)
    class_ref = ForeignKeyField(KharazmiClass, backref="users")
    max_easy = IntegerField(default=0)
    max_medium = IntegerField(default=0)
    max_hard = IntegerField(default=0)
    score_received = IntegerField(default=0)
    max_level1_score = IntegerField(default=0)
    max_level2_score = IntegerField(default=0)
    max_level3_score = IntegerField(default=0)
    max_level4_score = IntegerField(default=0)


db.create_tables([User], safe=True)
