from flask import Flask, request, jsonify
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

Candy(name="Licorice", flavor="Strawberry", shape="bites").save()
Candy(name="Sour Straws", flavor="Pink Lemonade", shape="long").save()
Candy(name="Lollipop", flavor="Rasberry", shape="sphere").save()
Candy(name="Twix", flavor="chocolate", shape="bites").save()
Candy(name="Jolly Rancher", flavor="Blue Rasperry", shape="tiny babies").save()
Candy(name="Cookies & Cream Chocolate bar", flavor="oreo chocolate", shape="bar").save()

app = Flask(__name__)

@app.route("/candy/", methods=["GET", "POST"])
@app.route("/candy/<id>", methods=["GET", "PUT", "DELETE"])
def endpoint(id=None):
    if request.method == "GET":
        if id:
            return jsonify(model_to_dict(Candy.get(Candy.id == id))
)