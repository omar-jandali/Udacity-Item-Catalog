"""
This file is the property of OmnaCore and was written by Omar Jandali

-- This file is the initial database setup up file which includes:
    -- main database - tastebuds
    -- initital databases = restaurant, dishes
"""

import os
import sys
from sqlalchemy import Conumn, String, Integer, ForeignKey, Index
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Restaurants(Base):
    __tablename__ = 'restaurants'

    id = Column(Integer, Primary_Key = True)
    name = Column(String(100), nullable = False, Unique = True, Index = True)

class Restaurants_Info(Base):
    __tablename__ = 'restaurants_info'

    id = Column(Integer, Primary_Key = True)
    food_type = Column(String(100), nullable = False)
    avg_price = Column(Integer(5), nullable = False)
    city = Column(String(100), nullable = False, Index = True)
    state = Column(String(3), nullable = False)
    restaurants_id = Column(Integer(100), ForeignKey('restaurants.id'))
    restaurants = relationship(Restaurants)

class Restaurants_Rating(Base):
    __tablename__ = 'restaurants_rating'

    id = Column(Integer, Primary_Key = True)
    restaurants_rating = Column(Integer(2), nullable = True)
    food_rating = Column(Integer(2), nullable = True)
    service_rating = Column(Integer(2), nullable = True)
    location_rating = Column(Integer(2), nullable = True)
    access_rating = Column(Integer(2), nullable = True)
    restaurants_id = Column(Integer(100), ForeignKey('restaurants.id'))
    restaurants = relationship(Restaurants)

class Dishes(Base):
    __tablename__ = 'dishes'

    id = Column(Integer, Primary_Key = True)
    name = Column(String(100), nullable = True, Unique = True, Index = True)

class Dishes_Info(Base):
    __tablename__ = 'dishes_info'

    id = Column(Integer, Primary_Key = True)
    course = Column(String(100), nullable = True)
    price = Column(Integer(6), nullable = True)
    description = Column(String(200), nullable = True)
    dishes_id = Column(Integer, ForeignKey('dishes.id'))
    dishes = relationship(Dishes)

class Dishes_Rating(Base):
    __tablename__ = 'dishes_rating'

    id = Column(Integer, Primary_Key = True)
    dishes_rating = Column(Integer(2), nullable = True)
    flavor_rating = Column(Integer(2), nullable = True)
    texture_rating = Column(Integer(2), nullable = True)
    appearence_rating = Column(Integer(2), nullable = True)
    price_rating = Column(Integer(2), nullable = True)
    restaurants_id = Column(Integer(100), ForeignKey('restaurants.id'))
    restaurants = relationship(Restaurants)

engine = create_engine('sqlite:///tastebuds.db')

Base.metadata.create_all(engine)
