from flask import Blueprint, request, redirect, render_template, url_for, jsonify
from flask.views import MethodView

from flask.ext.mongoengine.wtf import model_form
from server.models import User, Debt, Purchase
from server import app
import json

class UserAPI(MethodView):

    def get(self):
        return jsonify({'res': True, 'users': [{'name': user.name,
                                                'email': user.email,
                                                'phone': user.phone,
                                                'username': user.username} for user in User.objects]})

    def post(self):

        data = request.form
        if len(set(['name', 'email', 'phone', 'username']) &
               set([x for x in data])) == 4:
            user = User(name=data['name'], email=data[
                'email'], username=data['username'], phone=data['phone'])
            user.save()
            return jsonify({'res': True,
                            'user': {
                            'name': user.name,
                            'email': user.email,
                            'phone': user.phone,
                            'username': user.username
                            }}
                           )
        else:
            return jsonify({'res': False,
                            'message': 'No name or email'}
                           )


class PurchaseAPI(MethodView):

    def updateDebt(self, purchase):
        owes = []
        for person in purchase.buyins:
            debt = Debt.objects.get_or_create(user_from=purchase.payer,
                                              user_to=person,
                                              defaults={'amount': 0})[0]

            per_person_amount = purchase.cost / len(purchase.buyins)
            Debt.objects(id=debt.id).update_one(inc__amount=per_person_amount)
            debt.reload()
            owes.append({'person': person.username, 'amount': debt.amount})
        return {purchase.payer.username: owes}

    def get(self):
        pass

    def post(self):
        data = request.json
        if len(set(['name', 'cost', 'payer', 'buyins', 'time']) &
               set([x for x in data])) == 5:

            # Validate that users involved have accounts

                # Extract payer id
            payer = User.objects(username=data['payer'])
            payer_id = payer[0].id

                # Extract ids of those who buy in
            buyins = User.objects(username__in=data.getlist('buyins'))
            buyin_ids = map(lambda x: x.id, buyins)

            purchase = Purchase(name=data['name'],
                                cost=data['cost'],
                                payer=payer_id,
                                buyins=buyin_ids,
                                time=data['time'])
            purchase.save()

            debt_up_to_date = self.updateDebt(purchase)

            return jsonify({'res': True,
                            'messsage': 'Purchase added',
                            'debts': debt_up_to_date})
        return jsonify({'res': False,
                        'message': 'default'})

app.add_url_rule('/users/', view_func=UserAPI.as_view('users'))
app.add_url_rule('/purchases/', view_func=PurchaseAPI.as_view('purchases'))
