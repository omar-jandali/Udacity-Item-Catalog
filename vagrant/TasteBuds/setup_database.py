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
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

#The following is what will create the declarative_base base that will be imported to every tables
Base = declarative_base()

#The following
class Users(Base):
    __table__ = 'users'

    id = Colum(Integer, primary_key = True)
    user_name = Column(String(16), nullable = False, unique = True, index = True)

class User_Auth(Base):
    __table__ = 'user_auth'

    id = Column(Integer, primary_key = True)
    last_name = Column(String(16), nullable = False)
    first_name = Column(String(16), nullable = False)
    password = Column(String(225), nullable = False)

class User_Info(Base):

    __table__ = 'user_info'

    id = Column(Integer, primary_key = True)
    email = Column(String(50), nullable = False, index = True, unique = True)
    phone = Column(Integer(12), nullable = True, unique = True)
    age = Column(Integer(2), nullable = False)
    gender = Column(String(2), nullable = True)

class User_Location(Base):
    __table__ = 'user_location'

    id = Column(Integer, primary_key = True)
    street = Column(String(200), mullable = False)
    city = Column(String(35), nullable = False)
    state = Column(String(3), nullable = False)
    zip_code = Column(Integer(5), nullable = False, index = True)
