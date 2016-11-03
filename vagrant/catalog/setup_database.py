import os
import sys
from sqlalchemy import Column, String, Integer, ForeignKey, Index
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Categories(Base):
  __tablename__ = 'categories'

  id = Column(Integer, primary_key = True)
  category = Column(String(100), nullable = False, index = True, unique = True)

class Items(Base):
  __tablename__ = 'items'

  id = Column(Integer, primary_key = True)
  title = Column(String(100), unique = True)
  description = Column(String(225))
  category_name = Column(String(100), ForeignKey('categories.category'))
  category = relationship(Categories)

engine = create_engine('sqlite:///catelogs.db')

Base.metadata.create_all(engine)
