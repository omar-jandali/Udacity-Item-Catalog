import os
import sys
from sqlalchemy import Column, String, Integer, ForeignKey, Index
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key = True)
    username = Column(String(100), index = True)
    email = Column(String(225), nullable = False)
    profile_pic = Column(String(225), nullable = False)

    @property
    def serialize(self):
        return{
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'profile_picture': self.profile_pic,
        }

class Categories(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key = True)
    category = Column(String(100), nullable = False, index = True, unique = True)
    users_id = Column(Integer, ForeignKey('users.email'))
    users = relationship(Users)

    @property
    def serialize(self):
        return{
            'category': self.category,
        }

class Items(Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key = True)
    title = Column(String(100), unique = True)
    description = Column(String(225))
    category_name = Column(String(100), ForeignKey('categories.category'))
    category = relationship(Categories)
    users_id = Column(Integer, ForeignKey('users.email'))
    users = relationship(Users)

    @property
    def serialize(self):
        return{
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'category': self.category_name,
        }

engine = create_engine('sqlite:///catelogs.db')

Base.metadata.create_all(engine)
