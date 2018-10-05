from datetime import datetime
from itemcatalog import db
from flask_login import UserMixin
from flask_dance.consumer.backend.sqla import OAuthConsumerMixin


class User(db.Model, UserMixin):

    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(250), nullable=False)
    items = db.relationship('Item', backref='user', lazy=True)
    insert_date = db.Column(db.DateTime(), default=datetime.utcnow)
    update_date = db.Column(db.DateTime(), default=datetime.utcnow)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'insert_date': self.insert_date,
            'update_date': self.update_date
        }

    def __repr__(self):
        return '<User {}>'.format(self.name)


class OAuth(db.Model, OAuthConsumerMixin):

    __tablename__ = 'user_auth'

    user_id = db.Column(db.Integer, db.ForeignKey(User.id))
    user = db.relationship(User)
