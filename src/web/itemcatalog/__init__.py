import os
import config  # noqa:E401
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

if os.environ['ENV'] == 'production':
    app.config.from_object('config.settings.Prod')
else:
    app.config.from_object('config.settings.Dev')

db = SQLAlchemy(app)

from .models import user, category, item # noqa:E401

db.create_all()
db.session.commit()


@app.route("/")
@app.route("/home")
def home():
    return "<h1>Home Page</h1>"


@app.route("/about")
def about():
    return "<h1>About Page</h1>"
