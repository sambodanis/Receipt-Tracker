from flask import url_for

from server import db


class User(db.Document):
    username = db.StringField(max_length=255, unique=True)
    name = db.StringField(max_length=255)
    email = db.StringField(max_length=255)
    phone = db.StringField(max_length=255)


class Debt(db.Document):
    user_from = db.ReferenceField(User)
    user_to = db.ReferenceField(User)
    amount = db.FloatField()


class Purchase(db.Document):
    name = db.StringField(max_length=255)
    cost = db.FloatField(min_value=0)
    payer = db.ReferenceField(User)
    buyins = db.ListField(db.ReferenceField(User))
    time = db.DateTimeField()
