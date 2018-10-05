from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import datetime

Base = declarative_base()


class Items(Base):
    __tablename__ = 'Items'

    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    description = Column(String(4000))
    category_id = Column(Integer, ForeignKey('categorys.id'))
    categories = relationship(
        'category', backref='category_recipes', foreign_keys=[category_id])
    user_id = Column(Integer, ForeignKey('users.id'))
    users = relationship(
        'User', backref='user_recipes', foreign_keys=[user_id])
    insert_date = Column(DateTime(), default=datetime.utcnow)
    last_update = Column(DateTime(), default=datetime.utcnow)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'category_id': self.category_id,
            'user_id': self.user_id,
            'insert_date': self.insert_date,
            'last_update': self.last_update
        }