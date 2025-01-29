import os
from dotenv import load_dotenv
from peewee import Model, CharField, ForeignKeyField, SqliteDatabase

load_dotenv()

db_path = os.getenv("DB_PATH")
db_path_parent = os.path.dirname(db_path)
os.makedirs(db_path_parent, exist_ok=True)

db = SqliteDatabase(db_path)


class BaseModel(Model):
    class Meta:
        database = db


class KharazmiClass(BaseModel):
    class_name = CharField()


class User(BaseModel):
    username = CharField(unique=True)
    password = CharField()
    class_ref = ForeignKeyField(KharazmiClass, backref="users")


db.connect()
db.create_tables([User, KharazmiClass], safe=True)

KharazmiClass.create(class_name="A")
KharazmiClass.create(class_name="B")
KharazmiClass.create(class_name="C")
