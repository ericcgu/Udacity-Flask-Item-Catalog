from datetime import datetime
from . import db, ma
from sqlalchemy import exc
from sqlalchemy_utils import aggregated
from .item import Item, ItemSchema
from marshmallow import fields


class Category(db.Model):

    __tablename__ = 'category'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(500), nullable=False, unique=True)
    items = db.relationship('Item', backref='category', lazy=True)
    item_total = db.Column(db.Integer, nullable=False, default=0)
    insert_date = db.Column(db.DateTime(), default=datetime.utcnow)
    update_date = db.Column(db.DateTime(), default=datetime.utcnow)

    @aggregated('items', db.Column(db.Integer))
    def item_total(self):
        return db.func.count(Item.id)

    def __repr__(self):
        return '<Category {}>'.format(self.name)

    def __hash__(self):
        return hash(self.name)

    @classmethod
    def seed(cls, fake):
        category = Category(
            name=fake.state()
        )
        category.save()

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
        except exc.IntegrityError:
            db.session.rollback()


class CategorySchema(ma.ModelSchema):
    class Meta:
        model = Category
    items = fields.Nested(ItemSchema, many=True,
                          only=['id', 'name', 'description',
                                'insert_date', 'update_date'])
