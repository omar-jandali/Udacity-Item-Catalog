"""
***This file is property of OmnaCore and was written by Omar Jandali***

This is the database setup page from PayUp which contains all of the following sections
    Initial classes which contain all of the different tables
    Table definitions and names that will be used to store and display information to the user
    Contains the main engine that will be running the program
"""

#The following are all of the standard imports that are needed to run the database
import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Index
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

#The following is what will create the declarative_base base that will be imported to every tables
Base = declarative_base()

#The following is the user table which will store the users id and username
class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key = True)
    username = Column(String(16), nullable = False, unique = True, index = True)

class Tab_Event(Base):
    __tablename__ = 'tab_event'

    id = Column(Integer, primary_key = True)
    description = Column(String(200))
    amount = Column(String(10))#may be changed to a float or decimal value later on during development
    user_id = Column(Integer(10), ForeignKey('users.id'))
    users = relationship(Users)

"""
class Tab_Event(Base):
    __tablename__ = 'tab_event'

    id = Column(Integer, primary_key = True)
    description = Column(String(200))
    amount = Column(String(10))#may be changed to a float or decimal value later on during development
    tab_id = Column(Integer(10), ForeignKey('tabs.id'))
    tab = relationship(Tabs)

class User_Auth(Base):
    __tablename__ = 'user_auth'

    id = Column(Integer, primary_key = True)
    email = Column(String(50), nullable = False, index = True, unique = True)
    password = Column(String(225), nullable = False)
    user_id = Column(Integer(10), ForeignKey('users.id'), nullable = False)
    user = relationship(Users)

class User_Info(Base):
    __tablename__ = 'user_info'

    id = Column(Integer, primary_key = True)
    last_name = Column(String(16), nullable = False)
    first_name = Column(String(16), nullable = False)
    company_name = Column(String(100))
    phone = Column(Integer(12), nullable = True, unique = True)
    age = Column(Integer(2), nullable = False)
    user_id = Column(Integer(10), ForeignKey('users.id'), nullable = False)
    user = relationship(Users)

class User_Location(Base):
    __tablename__ = 'user_location'

    id = Column(Integer, primary_key = True)
    street = Column(String(200), nullable = False)
    city = Column(String(35), nullable = False)
    state = Column(String(3), nullable = False)
    zip_code = Column(Integer(5), nullable = False, index = True)
    user_id = Column(Integer(10), ForeignKey('users.id'), nullable = False)
    user = relationship(Users)

class Tabs(Base):
    __tablename__ = 'tabs'

    id = Column(Integer, primary_key = True)
    lender = Column(Integer(10), ForeignKey('users.id'), nullable = False)
    borrower = Column(Integer(10), ForeignKey('users.id'), nullable = False)


"""

engine = create_engine('sqlite:///payup.db')

Base.metadata.create_all(engine)
