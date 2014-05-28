from flask import url_for

from server import db


class User(db.Document):
    name = db.StringField(max_length=255)
    email = db.StringField(max_length=255)


class House(db.Document):
    people = db.ListField(db.ReferenceField(User))


class Debt(db.Document):
    user_from = db.ReferenceField(User)
    user_to = db.ReferenceField(User)
    amount = db.IntField()
