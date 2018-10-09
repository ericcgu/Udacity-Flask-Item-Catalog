from flask import (render_template, url_for,
                   redirect, Blueprint)
from flask_login import login_required
from itemcatalog import db
from itemcatalog.models.item import Item
from itemcatalog.forms.item import ItemForm
from flask_login import current_user

item = Blueprint('item', __name__)


@item.route("/item/create", methods=['GET', 'POST'])
@login_required
def create_item():
    form = ItemForm()
    if form.validate_on_submit():
        new_item = Item(name=form.name.data, description=form.description.data,
                        category_id=form.category.data.id,
                        user_id=current_user.id)
        db.session.add(new_item)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('create_item.html', form=form)
