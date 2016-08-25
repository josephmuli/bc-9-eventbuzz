import os
from datetime import datetime

from database import Event, Ticket, engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker




class EventsCrud(object):

	engine = create_engine('sqlite:///ebuzz.sqlite', echo = False)

	# create new session object for queries
	Session = sessionmaker()
	Session.configure(bind=engine)
	session = Session()

	def __init__(self):
		"""self.name = name
		self.start_date = start_date
		self.end_date = end_date
		self.venue = venue"""
		pass


	def create_event(self, arg):
		'''
		creates a new event instance
		'''
		# datetime.datetime.strptime('2012-05-12', '%Y-%m-%d')
		# creating a new event from Event class
		event_name = arg['<name>']
		start_date = datetime.strptime(arg['<start_date>'], "%d-%m-%Y" )
		end_date = datetime.strptime(arg['<end_date>'], "%d-%m-%Y" )
		venue = arg['<venue>']
		event = Event(name=event_name, start_date=start_date, end_date=end_date, venue=venue)

		try:
			# add event object to session for db commit

			EventsCrud.session.add(event)
			EventsCrud.session.commit()
			return "Event created"
		except Exception as e:
			print e
			raise e

	def delete_event(self, event_id):
		'''
		deletes event entry by ID provided
		'''
		# query item by id given
		deleted_item = EventsCrud.session.query(Event).filter_by(id == event_id).first()
		EventsCrud.session.delete(deleted_item)
		EventsCrud.session.commit()


	def list_events(self):
		'''
		returns all event entries 
		'''

		# query to get all data from the Event table
		events = EventsCrud.session.query(Event).all()
		
		return events


	def edit_event(self, event_id, **kwargs):
		'''
		edits an event given an id
		'''
		# first queries all items and gets the specific by id
		event_item = EventsCrud.session.query(Event).filter_by(id == event_id)
		# refer dict key
		event_item['event'] = kwargs['events']
		# commit changes to db
		event_item.EventsCrud.session.commit()


	def event_view(self, event_id):
		'''
		returns all ticket entries for specified event id
		'''
		event_tickets = EventsCrud.session.query(Ticket).filter_by(id == event_id)

		return event_tickets
