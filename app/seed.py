import random
from faker import Faker

from app import app
from models import db, Restaurant, RestaurantPizza, Pizza

fake = Faker()

with app.app_context():

    Restaurant.query.delete()
    RestaurantPizza.query.delete()
    Pizza.query.delete()

    restaurants = []
    for i in range(10):
        restaurant = Restaurant(
            name=fake.name(),
            address=fake.address()
        )

        restaurants.append(restaurant)
    db.session.add_all(restaurants)
    db.session.commit()

    restaurantPizzas = []

    for i in range(10):
        restaurantPizza = RestaurantPizza(
            price=random.randint(100, 5000),
            pizza_id=random.randint(1, 10),
            restaurant_id=random.randint(1, 10)
        )

        restaurantPizzas.append(restaurantPizza)

    db.session.add_all(restaurantPizzas)
    db.session.commit()

    pizzas = []
    for i in range(10):
        pizza = Pizza(
            name=fake.name(),
            price=random.randint(100, 1000)
        )

        pizzas.append(pizza)

    db.session.add_all(pizzas)
    db.session.commit()
