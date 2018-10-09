import os
import config  # noqa:E401
from flask import Flask
from flask_login import LoginManager
from faker import Faker


app = Flask(__name__)

# Environment Configuration
app.config.from_object('config.settings.' + os.environ['ENV'])

# User Session Management
login_manager = LoginManager(app)

# Database
from .models import db, user, category, item # noqa:E401
db.create_all()
db.session.commit()

# Seed Users and Categories in Database
if app.config['TESTING'] is True:
    fake = Faker()

    for _ in range(100):
        user.User.seed(fake)

    for _ in range(5):
        category.Category.seed(fake)

# Routes
from itemcatalog.routes.userauth import userauth # noqa:E401
from itemcatalog.routes.category import category # noqa:E401
from itemcatalog.routes.item import item # noqa:E401
from itemcatalog.routes.main import main # noqa:E401

app.register_blueprint(userauth)
app.register_blueprint(category)
app.register_blueprint(item)
app.register_blueprint(main)
