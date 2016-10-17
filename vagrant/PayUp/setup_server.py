"""
***This file is property of OmnaCore and was written by Omar Jandali***

This is the initial server and page directory for PayUp. Here is the list of different parts:
    All of the different path directories and the methods that are called based on the path
    all of the different routes based of the Flask Framework
    It also include the initiation of the server and the local port for running the project
        though my local machine
"""

#The following are all of the standard import for Flask as well as imports that allow the project
#   to access database and use CRUD
from flask import Flask, render_template
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from setup_database import Base, Users, User_Auth, User_Info, User_Location

#The following line is what initiates the flask app for this project
app = Flask(__name__)

engine = create_engine('sqlite:///payup.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

@

if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = 8080)
