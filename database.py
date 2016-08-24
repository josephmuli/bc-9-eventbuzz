import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Table, Column, Integer, String, MetaData, DateTime



# create a connection to database ebuzz, echo relieves all logging
engine = create_engine('sqlite:///ebuzz.sqlite', echo = False)

Base = declarative_base()

Session = sessionmaker()
Session.configure(bind=engine)
session = Session()





class Event(Base):
	__tablename__ = 'events'

	id = Column(Integer, primary_key=True)
	name = Column(String)
	start_date = Column(DateTime)
	end_date = Column(DateTime)
	venue = Column(String)


	def __init__(self, name, start_date, end_date, venue):
		self.name = name
		self.start_date = start_date
		self.end_date = end_date
		self.venue = venue


	def __repr__(self):
		return "<Event(name='%s', start_date='%s', end_date='%s', venue='%s')>"%(self.name, self.start_date, self.end_date, self.venue)



Base.metadata.create_all(engine)