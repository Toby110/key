from peewee import *

db = SqliteDatabase('./model/my_app.db')


class Book(Model):
    user = CharField()
    psw = TextField()
    token=CharField()

    class Meta:
        database = db
