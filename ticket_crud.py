import os

from database import Event, Ticket, engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class TicketsCrud(object):

	engine = create_engine('sqlite:///ebuzz.sqlite', echo = False)

	# create new session object for queries
	Session = sessionmaker()
	Session.configure(bind=engine)
	session = Session()


	def __init__(self):
		pass


	def create_ticket(self, type, event_name):

		ticko = Ticket(type, event_name)
		TicketsCrud.session.add(ticko)
		TicketsCrud.session.commit()
		return ticko


	@staticmethod
	def ticket_invalidate(t_id):
		'''
		invalidates a ticket instance
		'''
		ticko = TicketsCrud.session.query(Ticket).filter_by(id=t_id)


		try:
			ticko.is_valid = False

			TicketsCrud.session.add(ticko)
			TicketsCrud.session.commit()
			return "Ticket has been invalidated"
		except Exception as e:
			print e
			raise e
