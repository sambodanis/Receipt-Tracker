from flask import Flask
from flask.ext.mongoengine import MongoEngine
import json

settings_path = 'config/settings.json'
settings = json.loads(open(settings_path, 'r').read())
db_settings = settings['db_settings']

app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {"DB": db_settings['DB']}
app.config["SECRET_KEY"] = db_settings["SECRET"]

db = MongoEngine(app)

import server.views

if __name__ == '__main__':
    app.run()
