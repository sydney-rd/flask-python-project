from flask import flask, request, jsonify
from peewee import * 
from playhouse.shortcuts import model_to_dict, dict_to_model

db = PostgresqlDatabase("candybasket",
                        user="sydneydavid",
                        password="",
                        host="localhost",
                        port="5432"    )