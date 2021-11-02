from unittest import TestCase

from event_parser.reader import read_events
from event_parser.event import Event
from event_parser.person import Person
from event_parser.gender import Gender


class TestReader(TestCase):

    def test_read_events(self):
        test_file_path = 'src/tests/data/test_data.csv'
        person1 = Person(first_name='Jenny', last_name='Yuryshev',
                         gender=Gender.female, email='jyuryshev3@list-manage.com')
        person2 = Person(first_name='Simeon', last_name='Olech',
                         gender=Gender.not_given, email='solech4@github.com')
        person3 = Person(first_name='Georgina', last_name='Farlowe',
                         gender=Gender.other, email='gfarlowe5@diigo.com')

        result = [Event(id=4, person=person1, ip_adress='10.171.57.131'),
                  Event(id=5, person=person2, ip_adress='83.144.63.157'),
                  Event(id=6, person=person3, ip_adress='67.249.75.128')
                  ]

        self.assertEqual(read_events(test_file_path), result)
