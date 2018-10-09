from flask import Blueprint, render_template
from itemcatalog.models.category import Category


main = Blueprint('main', __name__)


@main.route('/')
@main.route("/home")
def index():
    categories = Category.query.order_by(Category.name.asc())
    return render_template('home.html', title='About', categories=categories)
