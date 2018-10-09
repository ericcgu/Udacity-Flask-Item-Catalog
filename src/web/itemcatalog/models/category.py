from datetime import datetime
from . import db
from sqlalchemy import exc
from sqlalchemy_utils import aggregated
from .item import Item


class Category(db.Model):

    __tablename__ = 'category'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(500), nullable=False, unique=True)
    item = db.relationship('Item', backref='category', lazy=True)
    item_total = db.Column(db.Integer, nullable=False, default=0)
    insert_date = db.Column(db.DateTime(), default=datetime.utcnow)
    update_date = db.Column(db.DateTime(), default=datetime.utcnow)

    @aggregated('item', db.Column(db.Integer))
    def item_total(self):
        return db.func.count(Item.id)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'name': self.name,
            'item_total': self.item_total,
            'insert_date': self.insert_date,
            'update_date': self.update_date
        }

    def __repr__(self):
        return '<Category {}>'.format(self.name)

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
