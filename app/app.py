#!/usr/bin/env python3

from flask import Flask, make_response
from flask_migrate import Migrate
from flask_cors import CORS
from flask_restful import Resource, Api

from models import db, Restaurant, RestaurantPizza, Pizza

app = Flask(__name__)
CORS(app)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)


class Home(Resource):
    def get(self):
        return make_response("<h1> Welcome to Pizza palace</h2>")


api.add_resource(Home, "/")
if __name__ == '__main__':
    app.run(port=5555)
