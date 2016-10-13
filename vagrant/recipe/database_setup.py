import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

#the following creates a class that can be inhereted when called
class Shelter(Base):
    # the first line simply call the tables name that is going to be defined - Restaurant
    __tablename__ = "shelter"

    #the following lines of code will set the default names and descriptions of the all the columns
    #that are going to end up being created in table above
    id = Column(Integer, primary_key = True)
    name = Column(String(250), nullable = True)
    address = Column(String(250))
    city = Column(String(20))
    state = Column(String(2))
    zip = Column(Integer(5))
    website = Column(String(250))


class Puppy(Base):
    __tablename__ = "Puppy"

    id = Column(Integer, primary_key = True)
    name = Column(String(80), nullable = False)
    dob = Column(Integer(8))
    gender = Column(String(5))
    weight = Column(Integer(4))
    shelter_id = Column(Integer, ForeignKey('shelter.id'))
    shelter = relationship(shelter)

#AT THE END OF THE FILE
engine = create_engine('sqlite:///restaurantment.db')

Base.metadata.create_all(engine)
