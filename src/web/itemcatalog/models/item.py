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
    time_inserted = db.Column(db.DateTime(), default=datetime.utcnow)
    time_updated = db.Column(db.DateTime(), default=datetime.utcnow)

    def __len__(self):
        return len(self)


class ItemSchema(ma.ModelSchema):
    class Meta:
        model = Item
