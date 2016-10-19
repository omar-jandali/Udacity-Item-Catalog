"""
This file is the property of OmnaCore and was written by Omar Jandali

-- This file is the initial server setup up file which includes:
    -- it will contain the Flask framework that will cover the following:
        -- all the routes and urls for the site
        -- all of the functions that will be handled for each of the pages
        -- all of the forms that will be used to CRUD the database records
"""

from flask import Flask, render_template, request, redirect, url_for, flash
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from setup_database import Base, Restaurants, Restaurants_Info, Restaurants_Rating, Dishes, Dishes_Info, Dishes_Rating

app = Flask(__name__)

engine = create_engine('sqlite:///tastebuds.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/test')
def testingPage():
    return 'This is just a test page to get the server running'

if __name__ == '__main__':
    app.secret_key = "Secret_Key"
    app.debug = True
    app.run(host = '0.0.0.0', port = 4040)
