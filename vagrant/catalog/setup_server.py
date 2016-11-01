from flask import Flask, render_template, request, redirect, url_for, flash
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from setup_database import Base, Categories, Items

app = Flask(__name__)

engine = create_engine('sqlite:///catelogs.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/testpage')
def TestPage():
  return render_template('testpage.html')

@app.route('/createcategory', methods=['GET', 'POST'])
def CreateCategory():
    if request.method == 'POST':
        newCategory = Categories(category = request.form['name'])
        session.add(newCategory)
        session.commit()
        return redirect(url_for('HomePage'))
    return render_template('createCategory.html')

@app.route('/')
def HomePage():
    categories = session.query(Categories).order_by(Categories.id)
    return render_template('homePage.html' categories = categories)

if __name__ == '__main__':
    app.secret_key = "Secret_Key"
    app.debug = True
    app.run(host = '0.0.0.0', port = 8000)
