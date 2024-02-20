#!/usr/bin/env python3

from flask import Flask, jsonify, make_response, request
from flask_migrate import Migrate
from flask_cors import CORS
from flask_restful import Resource, Api

from models import db, Restaurant, RestaurantPizza, Pizza

app = Flask(__name__)
api = Api(app)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)


class Home(Resource):
    def get(self):
        return make_response("<h1> Welcome to Pizza palace</h2>")


api.add_resource(Home, "/")


class Pizzas(Resource):
    def get(self):
        pizzas = [pizza.to_dict() for pizza in Pizza.query.all()]
        return make_response(jsonify(pizzas), 200)

    def post(self):
        data = request.get_json()
        new_pizza = Pizza(
            name=data.get("name"),
            price=data.get("price")
        )

        db.session.add(new_pizza)
        db.session.commit()

        return make_response(jsonify(new_pizza.to_dict()), 201)


api.add_resource(Pizzas, "/pizzas")


class PizzaById(Resource):
    def get(self, id):
        pizza = Pizza.query.filter_by(id=id).first()
        return make_response(jsonify(pizza.to_dict()), 200)

    def patch(self, id):
        pizza = Pizza.query.filter_by(id=id).first()

        data = request.get_json()
        for attr, value in data.items():
            setattr(pizza, attr, value)

        db.session.commit()

        return make_response(jsonify(pizza.to_dict()), 200)

    def delete(self, id):
        pizza = Pizza.query.filter_by(id=id).first()

        db.session.delete(pizza)
        db.session.commit()

        return make_response(["Pizza deleted"], 200)


api.add_resource(PizzaById, "/pizzas/<int:id>")


class Restaurants(Resource):
    def get(self):
        restaurants = [restaurant.to_dict()
                       for restaurant in Restaurant.query.all()]
        return make_response(jsonify(restaurants), 200)

    def post(self):
        data = request.to_dict()
        new_restaurant = Restaurant(
            name=data.get("name"),
            address=data.get("address")
        )
        db.session.add(new_restaurant)
        db.session.commit()

        return make_response(jsonify(new_restaurant).to_dict(), 201)


api.add_resource(Restaurants, "/restaurants")


class RestaurantById(Resource):
    def get(self, id):
        restaurant = Restaurant.query.filter_by(id=id).first()
        return make_response(jsonify(restaurant.to_dict()), 200)

    def patch(self, id):
        restaurant = Restaurant.query.filter_by(id=id).first()
        data = request.get_json()

        for attr, value in data.items():
            setattr(restaurant, attr, value)

        db.session.commit()

        return make_response(jsonify(restaurant.to_dict()), 200)

    def delete(self, id):
        restaurant = Restaurant.query.filter_by(id=id).first()
        db.session.delete(restaurant)
        db.session.commit()

        return make_response(["Restaurant deleted"], 200)


api.add_resource(RestaurantById, "/restaurants/<int:id>")
if __name__ == '__main__':
    app.run(port=5555)
