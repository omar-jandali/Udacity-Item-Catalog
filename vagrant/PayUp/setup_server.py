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
from flask import Flask, render_template, request, redirect, url_for, flash
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from setup_database import Base, Users, Tab_Event

#The following line is what initiates the flask app for this project
app = Flask(__name__)

engine = create_engine('sqlite:///payup.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/')
@app.route('/home')
def DisplayHome():
    return 'Welcome the the payup home page'

@app.route('/user/<int:user_id>')
def DisplayUsers(user_id):
    user = session.query(Users).filter_by(id = user_id).one()
    items = session.query(Tab_Event).filter_by(user_id = user.id)
    return render_template('viewTabs.html', user = user, items = items)

@app.route('/newtab/<int:user_id>', methods = ['GET', 'POST'])
def AddNewTab(user_id):
    if request.method == 'POST':
        newTab = Tab_Event(amount = request.form['amount'], description = request.form['description'], user_id = user_id)
        session.add(newTab)
        session.commit()
        flash("a new tab was just added")
        return redirect(url_for('DisplayUsers', user_id = user_id))
    return render_template('createTab.html', user_id = user_id)

@app.route('/edit/<int:user_id>/<int:tab_id>', methods = ['GET', 'POST'])
def EditTabEvent(user_id, tab_id):
    editTab = session.query(Tab_Event).filter_by(id = tab_id).one()
    if request.method == 'POST':
        if request.form['amount']:
            editTab.name = request.form['amount']
            session.add(editTab)
            session.commit()
            flash("a tab amount has been updated")
        if request.form['description']:
            editTab.description = request.form['description']
            session.add(editTab)
            session.commit()
            flash("a tab description has been updated")
        return redirect(url_for('DisplayUsers', user_id = user_id))
    else:
        return render_template('editTab.html', user_id = user_id, tab_id = tab_id, item = editTab)

@app.route('/delete/<int:user_id>/<int:tab_id>', methods = ['GET', 'POST'])
def DeleteTabEvent(user_id, tab_id):
    deleteTab = session.query(Tab_Event).filter_by(id = tab_id).one()
    if request.method == 'POST':
        session.delete(deleteTab)
        session.commit()
        flash("a tab was just deleted")
        return redirect(url_for('DisplayUsers', user_id = user_id))
    else:
        return render_template('deleteTab.html', user_id = user_id, item = deleteTab)

if __name__ == '__main__':
    app.secret_key = "Secret_Key"
    app.debug = True
    app.run(host = '0.0.0.0', port = 8080)
