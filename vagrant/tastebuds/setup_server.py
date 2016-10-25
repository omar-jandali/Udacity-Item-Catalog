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

@app.route('/home')
def DisplayRestaurant():
    restaurants = session.query(Restaurants).order_by(Restaurants.id)
    return render_template('displayRestaurants.html', restaurants = restaurants)

@app.route('/addrestaurant', methods=['GET', 'POST'])
def CreateRestaurant():
    if request.method == 'POST':
        newRestaurant = Restaurants(name = request.form['name'],
                                    city = request.form['city'],
                                    state = request.form['state'])
        session.add(newRestaurant)
        session.commit()
        flash('%s was successfully created' % newRestaurant.name)
        return redirect(url_for('DisplayRestaurant'))
    return render_template('addRestaurant.html')

@app.route('/<int:restaurant_id>/viewrestaurant')
def ViewRestaurant(restaurant_id):
    restaurants = session.query(Restaurants).filter_by(id = restaurant_id).one()
    rating = session.query(Restaurants_Rating).filter_by(restaurants_id = restaurant_id)
    return render_template('viewRestaurant.html', restaurant = restaurants, rating = rating)

@app.route('/<int:restaurant_id>/raterestaurant', methods = ['GET', 'POST'])
def RateRestaurant(restaurant_id):
    if request.method == 'POST':
        newRating = Restaurants_Rating(food_rating = request.form['food_rating'],
                                        service_rating = request.form['service_rating'],
                                        pricing_rating = request.form['pricing_rating'],
                                        location_rating = request.form['location_rating'],
                                        access_rating = request.form['access_rating'],
                                        restaurants_id = restaurant_id)
        session.add(newRating)
        session.commit()
        return redirect(url_for('ViewRestaurant', restaurant_id = restaurant_id))
    return render_template('rateRestaurant.html', restaurant_id = restaurant_id)

@app.route('/<int:restaurant_id>/edit', methods= ['GET', 'POST'])
def EditRestaurant(restaurant_id):
    editRestaurant = session.query(Restaurants).filter_by(id = restaurant_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editRestaurant.name = request.form['name']
        if request.form['city']:
            editRestaurant.city = request.form['city']
        if request.form['state']:
            editRestaurant.state = request.form['state']
        session.add(editRestaurant)
        session.commit()
        return redirect(url_for('DisplayRestaurant'))
    return render_template('editRestaurant.html', restaurant = editRestaurant)
    #return render_template('test.html')

@app.route('/<int:restaurant_id>/delete', methods=['GET', 'POST'])
def DeleteRestaurant(restaurant_id):
    deleteRestaurant = session.query(Restaurants).filter_by(id = restaurant_id).one()
    if request.method == 'POST':
        session.delete(deleteRestaurant)
        session.commit
        return redirect(url_for('DisplayRestaurant'))
    return render_template('deleteRestaurant.html', restaurant = deleteRestaurant)
    #return render_template('test.html')

@app.route('/<int:restaurant_id>/dishes')
def DisplayDishes(restaurant_id):
    restaurant = session.query(Restaurants).filter_by(id = restaurant_id).one()
    dishes = session.query(Dishes).filter_by(restaurant_id = restaurant.id)
    return render_template('displayDishes.html', restaurant = restaurant, dishes = dishes)

@app.route('/<int:restaurant_id>/addDish', methods = ['GET', 'POST'])
def CreateDish(restaurant_id):
    if request.method == 'POST':
        newDish = Dishes(name = request.form['name'],
                         price = request.form['price'],
                         description = request.form['description'],
                         restaurant_id = restaurant_id)
        session.add(newDish)
        session.commit()
        return redirect(url_for('DisplayDishes', restaurant_id = restaurant_id))
    return render_template('addDishes.html', restaurant_id = restaurant_id)

@app.route('/<int:restaurant_id>/<int:dish_id>/edit', methods=['GET', 'POST'])
def EditDish(restaurant_id, dish_id):
    editDish = session.query(Dishes).filter_by(id = dish_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editDish.name = request.form['name']
        if request.form['price']:
            editDish.price = request.form['price']
        if request.form['description']:
            editDish.description = request.form['description']
        session.add(editDish)
        session.commit()
        return redirect(url_for('DisplayDishes', restaurant_id = restaurant_id))
    return render_template('editDish.html', restaurant_id = restaurant_id, dish_id = dish_id, dish = editDish)
    #return render_template('test.html')

@app.route('/<int:restaurant_id>/<int:dish_id>/delete', methods=['GET', 'POST'])
def DeleteDish(restaurant_id, dish_id):
    deleteDish = session.query(Dishes).filter_by(id = dish_id).one()
    if request.method == 'POST':
        session.delete(deleteDish)
        session.commit
        return redirect(url_for('DisplayDishes', restaurant_id = restaurant_id))
    return render_template('deleteDish.html', restaurant_id = restaurant_id, dish = deleteDish)
    #return render_template('test.html')

if __name__ == '__main__':
    app.secret_key = "Secret_Key"
    app.debug = True
    app.run(host = '0.0.0.0', port = 8080)
