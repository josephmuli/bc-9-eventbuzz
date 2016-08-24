from database import Event
from sqlalchemy import sessionmaker




class EventsCrud(object):

	engine = create_engine('sqlite://ebuzz.sqlite', echo = False)
	
	# a new query session
	Session = sessionmaker(bind=engine)
	session = Session()


	def create_event(self):
		'''
		creates a new event
		'''
		# creating a new event from Event class
		event = Event(name, start_date, end_date, venue)

		# add event object to session
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