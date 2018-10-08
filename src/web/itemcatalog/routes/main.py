from flask import Blueprint
from flask_login import login_required, current_user


main = Blueprint('main', __name__)


@main.route('/')
@main.route("/home")
@login_required
def index():
    return '<h1>You are logged in as {}</h1>'.format(current_user.name)
