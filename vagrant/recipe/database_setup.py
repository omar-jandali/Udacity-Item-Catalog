import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

#the following creates a class that can be inhereted when called
class Restaurant(Base):
    # the first line simply call the tables name that is going to be defined - Restaurant
    __tablename__ = "restaurant"

    #the following lines of code will set the default names and descriptions of the all the columns
    #that are going to end up being created in table above
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=True)

class MenuItem(Base):
    __tablename__ = "menu_item"

    name = Column(String(80) nullable=False)
    id = Column(Integer, primary_key=True)
    description = Column(String(250))
    price = Column(String(8))
    course = Column(String(250))
    restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
    restaurant = relationship(Restaurant)

#AT THE END OF THE FILE
engine = create_engine('sqlite:///restaurantment.db')

Base.metadata.create_all(engine)
