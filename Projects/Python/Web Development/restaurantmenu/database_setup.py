###config code ### imports necessary modules
import sys
 
from sqlalchemy import Column,ForeignKey, Integer, String
#classes to use
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import relationship

from sqlalchemy import create_engine

#create instance of declarative base, which lets python know that objects are special base classes from sqlalchemy

Base = declarative_base()

###class code ### represents our data in python

class Restaurant(Base):

###table code ### represents a specific table in db

	__tablename__ = 'restaurant'

###mapper code ### conncects column of table to class that represents it

	name = Column(
	String(80), nullable = False)

	id = Column(
	Integer, primary_key = True)

class MenuItem(Base):

###table code ### represents a specific table in db

	__tablename__ = 'menu_item'

###mapper code ### conncects column of table to class that represents it

	name = Column(String(80), nullable = False)

	id = Column(Integer, primary_key = True)

	course = Column(String(250))

	description = Column(String(250))

	price = Column(String(8))

	restaurant_id = Column(Integer, ForeignKey('restaurant.id'))

	restaurant = relationship(Restaurant)


###config code ### creates/connects database

engine = create_engine('sqlite:///restaurantmenu.db')

Base.metadata.create_all(engine)
