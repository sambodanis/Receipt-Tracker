import requests
import json
import datetime

path = 'http://localhost:5000/'
user_path = path + 'users/'
purchase_path = path + 'purchases/'

json_header = {'content-type': 'application/json'}

users = [
    {'name': 'sam bodanis',
        'username': 'sam',
        'email': 'sam.bodanis@gmail.com',
        'phone': '1'},
    {'name': 'sahaj sawhney',
        'username': 'sahaj',
        'email': 'sahaj.sawhney@gmail.com',
        'phone': '2'},
    {'name': 'andrew stuart',
        'username': 'andy',
        'email': 'andy.stuart@gmail.com',
        'phone': '3'}
]

purchases = [
    {'name': 'apples',
        'cost': 3,
        'payer': 'sam',
        'buyins': ['sam', 'andy', 'sahaj'],
        'time': str(datetime.datetime.now())
     },
    {'name': 'bananas',
        'cost': 3.5,
        'payer': 'sam',
        'buyins': ['andy', 'sahaj'],
        'time': str(datetime.datetime.now())
     },
    {'name': 'blue cheese',
        'cost': 4,
        'payer': 'sam',
        'buyins': ['sam', 'andy'],
        'time': str(datetime.datetime.now())
     },
    {'name': 'ice cream',
        'cost': 3,
        'payer': 'sam',
        'buyins': ['sam'],
        'time': str(datetime.datetime.now())
     }
]

# for user in users:
#     r = requests.post(url=user_path, data=user)
#     print r.text

for purchase in purchases:
    r = requests.post(url=purchase_path, data=purchase)
    print r.text
