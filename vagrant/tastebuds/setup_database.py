"""
This file is the property of OmnaCore and was written by Omar Jandali

-- This file is the initial database setup up file which includes:
    -- main database - tastebuds
    -- initital databases = restaurant, dishes
"""

import os
import sys
from sqlalchemy import Column, String, Integer, ForeignKey, Index
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

#The following table will save all of the restaurants and their record id
class Restaurants(Base):
    __tablename__ = 'restaurants'

    id = Column(Integer, primary_key = True)
    name = Column(String(100), nullable = False, unique = True, index = True)
    city = Column(String(100), nullable = False, index = True)
    state = Column(String(3), nullable = False)

# the following class will store all of the restaurants general informaiton
class Restaurants_Info(Base):
    __tablename__ = 'restaurants_info'

    id = Column(Integer, primary_key = True)
    food_type = Column(String(100), nullable = False)
    avg_price = Column(Integer(5), nullable = False)
    restaurants_id = Column(Integer(100), ForeignKey('restaurants.id'))
    restaurants = relationship(Restaurants)

# the following table contains all of the different ratings that cover most aspects of the restaurant
class Restaurants_Rating(Base):
    __tablename__ = 'restaurants_rating'

    food = Column(String(100), nullable = True)
    service = Column(String(100), nullable = True)
    pricing = Column(String(100), nullable = True)
    location = Column(String(100), nullable = True)
    access = Column(String(100), nullable = True)
    restaurants_id = Column(Integer(100), ForeignKey('restaurants.id'))
    restaurants = relationship(Restaurants)

#The following table will asign and save the name and record id of each dish
class Dishes(Base):
    __tablename__ = 'dishes'

    id = Column(Integer, primary_key = True)
    name = Column(String(100), nullable = True, unique = True, index = True)
    price = Column(Integer(6), nullable = True)
    description = Column(String(200), nullable = True)
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'))
    restaurant = relationship(Restaurants)

#The following table will store and track all of the dishes general information
class Dishes_Info(Base):
    __tablename__ = 'dishes_info'

    id = Column(Integer, primary_key = True)
    course = Column(String(100), nullable = True)
    dishes_id = Column(Integer, ForeignKey('dishes.id'))
    dishes = relationship(Dishes)

#the following table will keep track of each dishes rating aspects
class Dishes_Rating(Base):
    __tablename__ = 'dishes_rating'

    id = Column(Integer,primary_key = True)
    dishes_rating = Column(Integer(2), nullable = True)
    flavor_rating = Column(Integer(2), nullable = True)
    texture_rating = Column(Integer(2), nullable = True)
    appearence_rating = Column(Integer(2), nullable = True)
    price_rating = Column(Integer(2), nullable = True)
    restaurants_id = Column(Integer(100), ForeignKey('restaurants.id'))
    restaurants = relationship(Restaurants)

engine = create_engine('sqlite:///tastebuds.db')

Base.metadata.create_all(engine)

"""
Potential changes:
    current - the user will put a rating for each of the different aspects of a dish or restaurant that
    they chose as well as a over rating [1-5]

        Restaurant [ 1-5 ]
        food [ 1-5 ]
        service [ 1-5 ]
        location [ 1-5 ]
        access [ 1-5 ]
        price [ 1-5 ]

    possibility - change to display a small chart to base the rating over and just one inputted ratio rather
    than several different ratios.

        food (0-.5-1)
        service (0-.5-1)
        location (0-.5-1)
        access (0-.5-1)
        pricing (0-.5-1)
        Restaurant [ 1-5 ]

"""
