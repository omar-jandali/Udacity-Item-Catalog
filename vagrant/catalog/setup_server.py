from flask import Flask, render_template, request, redirect, url_for, flash
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from setup_database import Base, Restaurants, Restaurants_Info, Restaurants_Rating, Dishes, Dishes_Info, Dishes_Rating

app = Flask(__name__)

engine = create_engine('sqlite:///catelogs.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/testpage')
def TestPage():
  return render_template('testpage.html')

if __name__ == '__main__':
    app.secret_key = "Secret_Key"
    app.debug = True
    app.run(host = '0.0.0.0', port = 8000)
