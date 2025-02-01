import os
import sys
from peewee import *

db_path = os.getenv("DB_PATH")
db_path_parent = os.path.dirname(db_path)
os.makedirs(db_path_parent, exist_ok=True)

db = SqliteDatabase(db_path)
db.connect()
