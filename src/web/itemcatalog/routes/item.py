from flask import (render_template, url_for,
                   redirect, Blueprint, abort, flash)
from flask_login import current_user, login_required
from itemcatalog import db
from itemcatalog.models.item import Item
from itemcatalog.forms.item import ItemForm


item = Blueprint('item', __name__)


@item.route("/item/create", methods=['GET', 'POST'])
@login_required
def create_item():
    """CREATE Item"""
    form = ItemForm()
    if form.validate_on_submit():
        new_item = Item(name=form.name.data, description=form.description.data,
                        category_id=form.category.data.id,
                        user_id=current_user.id)
        db.session.add(new_item)
        db.session.commit()
        flash('Your job listing has been successfully created!', 'success')
        return redirect(url_for('main.index'))
    return render_template('create_item.html', form=form)


@item.route("/item/<int:item_id>/delete", methods=['POST'])
@login_required
def delete_item(item_id):
    """
    DELETE Item
    :param item_id: item_id (int) for Item
    """
    item = Item.query.get_or_404(item_id)
    if item.user != current_user:
        abort(403)
    db.session.delete(item)
    db.session.commit()
    flash('Your job listing has been successfully deleted!', 'success')
    return redirect(url_for('main.index'))
