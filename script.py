from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from sqlalchemy import *
from json import dumps

db_connect = create_engine('sqlite:///exemplo.db')
app = Flask(__name__)
api = Api(app)