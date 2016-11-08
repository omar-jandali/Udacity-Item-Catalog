"""
This is a big project that was completely written by Omar Jandali.

This file is a large one that can be overwhelming:
There are comments throughtout the document that will help clarify what each part of code does

All of the following code is written in PYTHON

for instructions on loading this document please look at the README.md file
"""

"""
The following are all of the different files and libraries that were imported and
implimented into this web project
"""
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from setup_database import Base, Categories, Items, Users

app = Flask(__name__)

from flask import session as login_session
import random, string

from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
from oauth2client.client import AccessTokenCredentials
import httplib2
import json
from flask import make_response
import requests

"""
The following are the database conections and google conneciton for the google plus login
"""

CLIENT_ID = json.loads(open('client_secrets.json', 'r').read())['web']['client_id']

engine = create_engine('sqlite:///catelogs.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

"""
This is the home route: displays the homepage (categories and recently added items)
"""
@app.route('/')
@app.route('/home')
def HomePage():
    categories = session.query(Categories).order_by(Categories.id)
    items = session.query(Items).order_by(Items.id)
    if 'username' not in login_session:
        return render_template('publicHomePage.html', categories = categories, items = items)
    return render_template('homePage.html', categories = categories, items = items)

"""
This is the new item route: this is where new items are created once you log in
"""
@app.route('/createitem', methods = ['GET', 'POST'])
def AddItem():
    if 'username' not in login_session:
        return redirect('/login')
    categories = session.query(Categories).order_by(Categories.id)
    if request.method == 'POST':
        newItem = Items(title = request.form['title'],
                        description = request.form['description'],
                        category_name = request.form['category_name'],
                        users_id = login_session['email'])
        session.add(newItem)
        session.commit()
        return redirect(url_for('HomePage'))
    return render_template('createItems.html', categories = categories)

"""
This is the edit item route: this is where the user that create the item can make edits to
"""
@app.route('/<string:item_category>/<string:item_title>/edit', methods=['GET', 'POST'])
def EditItem(item_category, item_title):
    if 'username' not in login_session:
        return redirect('/login')
    categories = session.query(Categories).order_by(Categories.id)
    editedItem = session.query(Items).filter_by(title = item_title).one()
    if request.method == 'POST':
        if request.form['title']:
            editedItem.title = request.form['title']
        if request.form['description']:
            editedItem.description = request.form['description']
        if request.form['category_name']:
            editedItem.category_name = request.form['category_name']
        session.add(editedItem)
        session.commit()
        return redirect(url_for('HomePage'))
    return render_template('editItem.html', item_category = item_category, categories = categories, editedItem = editedItem)

"""
This is the delete item route: this is where the user that create the item and delete the item
"""
@app.route('/<string:item_category>/<string:item_title>/delete', methods=['GET', 'POST'])
def DeleteItem(item_category, item_title):
    categories = session.query(Categories).order_by(Categories.id)
    deleteItem = session.query(Items).filter_by(title = item_title).one()
    if 'username' not in login_session:
        return redirect('/login')
    if request.method == 'POST':
        session.delete(deleteItem)
        session.commit()
        return redirect(url_for('HomePage'))
    return render_template('deleteItem.html', item_category = item_category, deleteItem = deleteItem, categories = categories)

"""
This is the show items route: this will show all the items in a selected categories
"""
@app.route('/catalog/<string:category>/items')
def ShowItems(category):
    categories = session.query(Categories).order_by(Categories.id)
    items = session.query(Items).filter_by(category_name = category)
    return render_template('ShowCategoryItems.html', items = items, category = category, categories = categories)

"""
THis is the selected items route: this route will show the details about a specific items that the user selected
"""
@app.route('/catalog/<string:category>/<string:item>')
def SelectedItem(category, item):
    categories = session.query(Categories).order_by(Categories.id)
    selecteditem = session.query(Items).filter_by(title = item).one()
    if 'username' not in login_session:
        return render_template('publicShowSelectedItem.html', item = selecteditem, category = category,  categories = categories)
    if login_session['email'] != selecteditem.users_id:
        return render_template('publicShowSelectedItem.html', item = selecteditem, category = category,  categories = categories)
    return render_template('ShowSelectedItem.html', item = selecteditem, category = category, categories = categories)

"""
This is the login route: This route is where the user can login to the Google + login (only current option)
"""
@app.route('/login')
def Login():
    categories = session.query(Categories).order_by(Categories.id)
    state = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in xrange(32))
    login_session['state'] = state
    return render_template('login.html', STATE = state, categories = categories)

"""
This is the google connect route: this route is how the user logs into the google plus account
"""
@app.route('/gconnect', methods=['POST'])
def gconnect():
    # Validate state token
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    # Obtain authorization code
    code = request.data

    try:
        # Upgrade the authorization code into a credentials object
        oauth_flow = flow_from_clientsecrets('client_secrets.json', scope='')
        oauth_flow.redirect_uri = 'postmessage'
        credentials = oauth_flow.step2_exchange(code)
    except FlowExchangeError:
        response = make_response(
            json.dumps('Failed to upgrade the authorization code.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Check that the access token is valid.
    access_token = credentials.access_token
    url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s'
           % access_token)
    h = httplib2.Http()
    result = json.loads(h.request(url, 'GET')[1])
    # If there was an error in the access token info, abort.
    if result.get('error') is not None:
        response = make_response(json.dumps(result.get('error')), 500)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is used for the intended user.
    gplus_id = credentials.id_token['sub']
    if result['user_id'] != gplus_id:
        response = make_response(
            json.dumps("Token's user ID doesn't match given user ID."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is valid for this app.
    if result['issued_to'] != CLIENT_ID:
        response = make_response(
            json.dumps("Token's client ID does not match app's."), 401)
        print "Token's client ID does not match app's."
        response.headers['Content-Type'] = 'application/json'
        return response

    stored_credentials = login_session.get('credentials')
    stored_gplus_id = login_session.get('gplus_id')
    if stored_credentials is not None and gplus_id == stored_gplus_id:
        response = make_response(json.dumps('Current user is already connected.'),
                                 200)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Store the access token in the session for later use.
    login_session['credentials'] = credentials.access_token
    login_session['gplus_id'] = gplus_id

    # Get user info
    userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    params = {'access_token': credentials.access_token, 'alt': 'json'}
    answer = requests.get(userinfo_url, params=params)

    data = json.loads(answer.text)

    login_session['username'] = data['name']
    login_session['picture'] = data['picture']
    login_session['email'] = data['email']

    output = ''
    output += '<h1>Welcome, '
    output += login_session['username']
    output += '!</h1>'
    output += '<img src="'
    output += login_session['picture']
    output += ' " style = "width: 300px; height: 300px;border-radius: 150px;-webkit-border-radius: 150px;-moz-border-radius: 150px;"> '
    flash("you are now logged in as %s" % login_session['username'])
    print "done!"
    return output

"""
This is the google disconnect route: this is where you will disconnect or logout from your google plus accoutn
"""
@app.route('/gdisconnect')
def gdisconnect():
    credentials = login_session.get('credentials')
    print credentials
    if credentials is None:
        response = make_response(json.dumps('Current user not connection'), 401)
        response.headersp['Content-Type'] = 'application/json'
        return response
    #access_token = credentials.access_token
    url = 'https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s' % credentials
    h = httplib2.Http()
    result = h.request(url, 'GET')[0]

    if result['status'] == '200':
        del login_session['credentials']
        del login_session['gplus_id']
        del login_session['username']
        del login_session['email']
        del login_session['picture']

        response = make_response(json.dumps('Successfully disconnected'), 200)
        response.headers['Content-Type'] = 'application/json'
        return response
    else:
        response = make_response(json.dumps('Failed to revoke token for given user'), 400)
        response.headers['Content-Type'] = 'application/json'
        return response

def CreateUser(login_session):
    newUser = Users(username = login_session['username'],
                    email = login_session['email'],
                    profile_pic = login_session['picture'])
    session.add(newUser)
    session.commit()
    user = session.query(Users).filter_by(email = login_session['email']).one()
    return user.id

def getUserInfo(user_id):
    user = session.query(Users).filter_by(id = user_id).one()
    return user

def getUserId(email):
    try:
        user = session.query(Users).filter_by(email = email).one()
        return user.id
    except:
        return None


"""
The following two routes are to get the jsonified records for categories and items
"""
@app.route('/catalog/<string:categories_name>/items/JSON')
def categoryItemsJSON(categories_name):
    categories = session.query(Categories).filter_by(category = categories_name).one()
    items = session.query(Items).filter_by(category_name = categories_name).all()
    return jsonify(CategoryItems = [i.serialize for i in items])

@app.route('/catalog/<string:categories_name>/<string:item>/JSON')
def signleItemJSON(categories_name, item):
    categories = session.query(Categories).filter_by(category = categories_name).one()
    item = session.query(Items).filter_by(title = item).one()
    return jsonify(SingleItem = item.serialize)

"""
-- uncomment the following  route if you would like to add more categories to the list --

@app.route('/createcategory', methods=['GET', 'POST'])
def CreateCategory():
    if request.method == 'POST':
        newCategory = Categories(category = request.form['name'],
        users_id = 1)
        session.add(newCategory)
        session.commit()
        return redirect(url_for('HomePage'))
        return render_template('createCategory.html')
"""

if __name__ == '__main__':
    app.secret_key = "Secret_Key"
    app.debug = True
    app.run(host = '0.0.0.0', port = 8000)
