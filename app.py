from flask import flask, request, jsonify
from peewee import * 
from playhouse.shortcuts import model_to_dict, dict_to_model

db = PostgresqlDatabase("candybasket",
                        user="sydneydavid",
                        password="",
                        host="localhost",
                        port="5432")

class BaseModel(Model):
    class Meta:
        database = db

class Candy(BaseModel):
    name = CharField()
    flavor = CharField()
    shape = CharField()

db.connect()
db.drop_tables([Candy])
db.create_tables([Candy])