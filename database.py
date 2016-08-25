import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import Table, Column, Integer, String, MetaData, DateTime
from sqlalchemy import ForeignKey


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

class Ticket(Base):
	__tablename__ = 'ticket'
	id = Column(Integer, primary_key=True)
	type = Column(String)
	event_id = Column(String, ForeignKey('events.id'))
	
	# defines relationship between models
	ticket_id = relationship("Event")



	def __init__(self, type, event_id):
		self.type = type
		self.event_id = event_id


Base.metadata.create_all(engine)