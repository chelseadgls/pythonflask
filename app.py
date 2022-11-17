from flask import Flask, jsonify, request
from peewee import *
from playhouse.shortcuts import model_to_dict, dict_to_model

db = PostgresqlDatabase('pokemon', user='', password='',
                        host='localhost', port=5432)


class BaseModel(Model):
    class Meta:
        database = db


class Pokemon(BaseModel):
    name = CharField()
    number = IntegerField()
    type = CharField()


db.connect
db.drop_tables([Pokemon])
db.create_tables([Pokemon])

Pokemon(name='Bulbasauer', number=1, type='grass').save()
Pokemon(name='Charmander', number=4, type='fire').save()
Pokemon(name='Squirtle', number=7, type='water').save()

app = Flask(__name__)

# routes

app.run(debug=True, port=9000)
