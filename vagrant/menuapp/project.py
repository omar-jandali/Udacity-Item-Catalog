#The following is the very basic / minial version of a flask app#

#the following two lines of code will import the framwork and create an instance
#of the framework called app
from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

app = Flask(__name__)

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# the following are wrap functions that are created by the Flask Framework

# if wither of the two routes are accessed, it will activate or trigger the HellowWOrld
# function that is defined below
@app.route('/')
@app.route('/hello')
@app.route('/restaurants/<int:restaurant_id>/')

def restaurantMenu(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id = restaurant_id).one()
    items = session.query(MenuItem).filter_by(restaurant_id = restaurant_id)

    output = ''
    for obj in items:
        output += obj.name
        output += '</br>'
    return output

# Task 1: Create route for newMenuItem function here
@app.route('/restaurant/<int:restaurant_id>/new')
def newMenuItem(restaurant_id):
    return "page to create a new menu item. Task 1 complete!"

# Task 2: Create route for editMenuItem function here
@app.route('/restaurant/<int:restaurant_id>/<int:menu_id>/edit/')
def editMenuItem(restaurant_id, menu_id):
    return "page to edit a menu item. Task 2 complete!"

# Task 3: Create a route for deleteMenuItem function here
@app.route('/restaurant/<int:restaurant_id>/<int:menu_id>/delete/')
def deleteMenuItem(restaurant_id, menu_id):
    return "page to delete a menu item. Task 3 complete!"

#the following well set the server port
#the webserver will only run of the function is directly run from this application and not imported
if __name__ == '__main__':
    app.debug = True
    #initialize the server port to run, it is inly run from the local machine and nothing else
    #the following line also will reset the server every time there is a change in code
    app.run(host = '0.0.0.0', port = 5000)
