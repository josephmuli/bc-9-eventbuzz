import os

from database import Event, engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker




class EventsCrud(object):

	engine = create_engine('sqlite:///ebuzz.sqlite', echo = False)

	# create new session object for queries
	Session = sessionmaker()
	Session.configure(bind=engine)
	session = Session()

	def __init__(self, name, start_date, end_date, venue):
		self.name = name
		self.start_date = start_date
		self.end_date = end_date
		self.venue = venue

	

	def create_event(self, name, start_date, end_date, venue):
		'''
		creates a new event instance
		'''
		# creating a new event from Event class
		event = Event(name, start_date, end_date, venue)

		# add event object to session for db commit
		EventsCrud.session.add(event)
		EventsCrud.session.commit()


	def delete_event(self, event_id):
		'''
		deletes event entry by ID provided
		'''
		# query item by id given
		deleted_item = EventsCrud.session.query(Event).filter(Event.id == event_id)
		EventsCrud.session.delete(deleted_item='evaluate')
		EventsCrud.session.commit()


	def list_events(self):
		'''
		returns all event entries 
		'''
		events = EventsCrud.session.query.all()
		return events

