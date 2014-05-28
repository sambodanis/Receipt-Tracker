from flask import Blueprint, request, redirect, render_template, url_for, jsonify
from flask.views import MethodView

from flask.ext.mongoengine.wtf import model_form
from server.models import User, House, Debt
from server import app


class UserAPI(MethodView):

    def get(self):
        return jsonify({'res': True, 'users': [u.name for u in User.objects]})

    def post(self):
        data = request.form
        print data
        if 'name' in data and 'email' in data:
            user = User(name=data['name'], email=data['email'])
            user.save()
            return jsonify({'res': True,
                            'user': {
                            'name': user.name,
                            'email': user.email
                            }})
        else:
            return jsonify({'res': False,
                            'message': 'No name or email'}
                           )


class HouseAPI(MethodView):

    def get(self):
        print House.objects

        jsonify({'res': True, 'users': [u.name for u in House.objects]})

    def post(self):
        people = request.form
        ids = User.objects(name__in=[person for person in people])
        if len(ids) != len(people):
            return jsonify({'res': False,
                            'message': 'Invalid data in housemates'}
                           )
        ids = map(lambda x: x.id, ids)
        house = House(people=ids)
        house.save()
        return jsonify({'res': True,
                        'house': [x.name for x in house.people]})

app.add_url_rule('/users/', view_func=UserAPI.as_view('users'))
app.add_url_rule('/houses/', view_func=HouseAPI.as_view('house'))
