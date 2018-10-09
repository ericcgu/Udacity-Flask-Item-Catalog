from datetime import datetime
from . import db
from sqlalchemy import exc


class Category(db.Model):
    __tablename__ = 'category'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(500), nullable=False, unique=True)
    items = db.relationship('Item', backref='category', lazy=True)
    insert_date = db.Column(db.DateTime(), default=datetime.utcnow)
    update_date = db.Column(db.DateTime(), default=datetime.utcnow)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'name': self.name,
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
