from flask import Blueprint, render_template
from itemcatalog.models.category import Category
from itemcatalog.models.item import Item

main = Blueprint('main', __name__)


@main.route('/')
@main.route("/home")
def index():
    """returns all items and categories"""
    categories = Category.query.filter(Category.item_total.isnot(None)).order_by(Category.name.asc()) # noqa:501
    items = Item.query.order_by(Item.update_date.desc())
    return render_template('main.html', title='Home', categories=categories,
                           items=items)
