from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)


class Restaurant(db.Model, SerializerMixin):
    __tablename__ = 'restaurants'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    address = db.Column(db.String)

    restaurantPizzas = db.relationship(
        "RestaurantPizza", back_populates="restaurant")

    def __repr__(self) -> str:
        return f"{self.name} and {self.address}"


class RestaurantPizza(db.Model, SerializerMixin):
    __tablename__ = "restaurantPizzas"

    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    pizza_id = db.Column(db.Integer, db.ForeignKey("pizzas.id"))
    restaurant_id = db.Column(db.Integer, db.ForeignKey("restaurants.id"))

    restaurant = db.relationship(
        "Restaurant", back_populates="restaurantPizzas")
    pizza = db.relationship("Pizza", back_populates="restaurantPizzas")

    def __repr__(self):
        return f"{self.price}"


class Pizzas(db.Model, SerializerMixin):
    __tablename__ = "pizzas"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    price = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    restaurantPizzas = db.relationship(
        "RestaurantPizza", back_populates="pizza")

    def __repr__(self):
        return f"{self.name} and {self.price}"
