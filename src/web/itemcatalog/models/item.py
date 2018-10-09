from datetime import datetime
from . import db, ma


class Item(db.Model):

    __tablename__ = 'item'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(4000))
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'),
                            nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),
                        nullable=False)
    insert_date = db.Column(db.DateTime(), default=datetime.utcnow)
    update_date = db.Column(db.DateTime(), default=datetime.utcnow)

    def __repr__(self):
        return '<Item {}>'.format(self.name)

    def __hash__(self):
        return hash(self.name)


class ItemSchema(ma.ModelSchema):
    class Meta:
        model = Item
