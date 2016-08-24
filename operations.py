from database import Event
from sqlalchemy import sessionmaker




class EventsCrud(object):

	engine = create_engine('sqlite://ebuzz.sqlite', echo = False)
	
	# a new query session
	Session = sessionmaker(bind=engine)
	session = Session()


	def create_event(self):
		
		# creating a new event from Event class
		event = Event(name, start_date, end_date, venue)

		# add event object to session
		session.add(event)
		session.commit()



