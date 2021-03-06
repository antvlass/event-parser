from unittest import TestCase
from ipaddress import IPv4Address

from event_parser.event import Event
from event_parser.person import Person
from event_parser.gender import Gender


class TestEvent(TestCase):

    def test_id(self):
        person = Person(first_name='O', last_name='V',
                        email='aa', gender=Gender.other)
        event = Event(id=999, person=person, ip_adress='10.171.57.131')

        self.assertEqual(event.id, 999)

    def test_person(self):
        person = Person(first_name='O', last_name='V',
                        email='aa', gender=Gender.other)
        event = Event(id=1, person=person, ip_adress='10.171.57.131')

        self.assertEqual(event.person, person)
        self.assertEqual(event.person.email, 'aa')

    def test_ip_adress(self):
        person = Person(first_name='O', last_name='V',
                        email='aa', gender=Gender.other)
        event = Event(id=1, person=person, ip_adress='10.171.57.131')

        self.assertEqual(event.ip_adress, IPv4Address("10.171.57.131"))

        event.ip_adress = IPv4Address("2.85.18.210")
        self.assertEqual(event.ip_adress, IPv4Address("2.85.18.210"))
        self.assertEqual(event.ip_adress.is_private, False)
