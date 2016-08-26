import unittest
from operations import EventsCrud
from database import Event


class EventTests(unittest.TestCase):



	def test_for_object_instance(self):
		event = Event(1,'rave', 12-05-2016, 18-05-2016)
		self.assertIsInstance(event, Event, msg="Check class Instance")