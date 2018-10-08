from flask import (render_template, url_for,
                   redirect, Blueprint)
from flask_login import login_required
from itemcatalog import db
from itemcatalog.models.category import Category
from itemcatalog.forms.category import CategoryForm

category = Blueprint('category', __name__)


@category.route("/category/new", methods=['GET', 'POST'])
@login_required
def new_category():
    form = CategoryForm()
    if form.validate_on_submit():
        new_category = Category(name=form.name.data, desc=form.desc.data)
        db.session.add(new_category)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('create_category.html', title='New Category',
                           form=form, legend='New Category')
