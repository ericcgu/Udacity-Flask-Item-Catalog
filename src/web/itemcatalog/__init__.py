import os
import config  # noqa:E401
from flask import Flask, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_dance.contrib.google import make_google_blueprint, google

app = Flask(__name__)

# Environment Configuration
if os.environ['ENV'] == 'production':
    app.config.from_object('config.settings.Prod')
else:
    app.config.from_object('config.settings.Dev')

# Database
db = SQLAlchemy(app)
from .models import user, category, item # noqa:E401
db.create_all()
db.session.commit()

# Auth
app.secret_key = app.config['GOOGLE_OAUTH_CLIENT_SECRET']

google_blueprint = make_google_blueprint(
    client_id=app.config['GOOGLE_OAUTH_CLIENT_ID'],
    client_secret=app.secret_key,
    scope=app.config['GOOGLE_OAUTH_CLIENT_SCOPE']
    )


@app.route("/")
@app.route("/home")
def home():
    return "<h1>Home Page</h1>"


@app.route("/glogin")
def index():
    if not google.authorized:
        return redirect(url_for("google.login"))
    resp = google.get(app.config['GOOGLE_OAUTH_CLIENT_USERINFO_URI'])
    assert resp.ok, resp.text
    return "You are {email} on Google".format(email=resp.json()["email"])
