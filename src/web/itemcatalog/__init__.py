import os
import config  # noqa:E401
from flask import Flask
from flask_login import LoginManager

from itemcatalog.routes.main import main

app = Flask(__name__)

# Environment Configuration
app.config.from_object('config.settings.' + os.environ['ENV'])

# User Session Management
login_manager = LoginManager(app)

# Database
from .models import db, user, category, item # noqa:E401
db.create_all()
db.session.commit()

# Auth
from itemcatalog.routes.userauth import userauth # noqa:E401
app.register_blueprint(userauth)

app.register_blueprint(main)
