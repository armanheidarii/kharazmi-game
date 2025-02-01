from peewee import CharField

from main.db import db
from main.db.models.Base import BaseModel


class KharazmiClass(BaseModel):
    class_name = CharField()


db.create_tables([KharazmiClass], safe=True)

KharazmiClass.create(class_name="A")
KharazmiClass.create(class_name="B")
KharazmiClass.create(class_name="C")
