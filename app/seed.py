import random
from faker import Faker

from app import app
from models import db, Restaurant, RestaurantPizza, Pizzas

fake = Faker()

with app.app_context():
    pass
