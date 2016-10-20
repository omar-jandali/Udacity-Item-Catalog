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

@app.route('/addrestaurant', methods=['GET', 'POST'])
def CreateRestaurant():
    if request.method == 'POST':
        newRestaurant = Restaurants(name = request.form['name'])
        session.add(newRestaurant)
        session.commit()
        newRestaurantInfo = Restaurants_Info(food_type = request.form['food_type'],
                                             avg_price = request.form['avg_price'],
                                             city = request.form['city'],
                                             state = request.form['state'])
        session.add(newRestaurantInfo)
        session.commit
        flash('%s was successfully created' % newRestaurant.name)
        return redirect(url_for('DisplayRestaurant'))
    else:
        return render_template('addRestaurant.html')

@app.route('/restaurants')
def DisplayRestaurant():
    restaurants = session.query(Restaurants).order_by(Restaurants.name)
    return render_template('displayRestaurants.html', restaurants = restaurants)

if __name__ == '__main__':
    app.secret_key = "Secret_Key"
    app.debug = True
    app.run(host = '0.0.0.0', port = 8080)
