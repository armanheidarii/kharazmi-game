from peewee import IntegerField, ForeignKeyField

from main.db import db
from main.db.models.Base import BaseModel
from main.db.models.User import User


class Game(BaseModel):
    game_level = IntegerField()
    level1_score = IntegerField()
    level2_score = IntegerField()
    level3_score = IntegerField()
    level4_score = IntegerField()
    final_score = IntegerField()
    user = ForeignKeyField(User, backref="games")


db.create_tables([Game], safe=True)
