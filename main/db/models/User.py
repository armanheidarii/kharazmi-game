from peewee import CharField, ForeignKeyField

from main.db import db
from main.db.models.Base import BaseModel
from main.db.models.KharazmiClass import KharazmiClass


class User(BaseModel):
    username = CharField(unique=True)
    password = CharField()
    email = CharField(null=True)
    class_ref = ForeignKeyField(KharazmiClass, backref="users")


db.create_tables([User], safe=True)
