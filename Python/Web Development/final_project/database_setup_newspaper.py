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

class Subject(Base):

###table code ### represents a specific table in db

	__tablename__ = 'subject'

###mapper code ### conncects column of table to class that represents it

	name = Column(
	String(80), nullable = False)

	id = Column(
	Integer, primary_key = True)

class Article(Base):

###table code ### represents a specific table in db

	__tablename__ = 'article'

###mapper code ### conncects column of table to class that represents it

	headline = Column(String(120), nullable = False)

	id = Column(Integer, primary_key = True)

	abstract = Column(String(250))

	source = Column(String(250))

	wordcount = Column(String(8))

	url = Column(String(120))

	subject_id = Column(Integer, ForeignKey('subject.id'))

	subject = relationship(Subject)



	@property 
	def serialize(self):
		#returns object data in easily serializable format
		return{
			'name' : self.headline,
			'abstract' : self.abstract,
			'id' : self.id,
			'wordcount' : self.wordcount,
			
		}


###config code ### creates/connects database

engine = create_engine('sqlite:///newspaper.db')

Base.metadata.create_all(engine)