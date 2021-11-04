from unittest import TestCase
from ipaddress import IPv4Address

from event_parser.reader import read_events, gender_normalization, ip_anonymization
from event_parser.event import Event
from event_parser.person import Person
from event_parser.gender import Gender


class TestReader(TestCase):
    def test_ip_anonymization(self):
        self.assertEqual(ip_anonymization(IPv4Address(
            "10.171.57.131")), IPv4Address("10.171.57.0"))

        self.assertEqual(ip_anonymization(IPv4Address(
            "86.69.117.124")), IPv4Address("86.69.117.0"))

        self.assertEqual(ip_anonymization(IPv4Address(
            "110.184.3.0")), IPv4Address("110.184.3.0"))

    def test_gender_normalization(self):
        self.assertEqual(gender_normalization("Female"), Gender.female)
        self.assertEqual(gender_normalization("MALE"), Gender.male)
        self.assertEqual(gender_normalization(None), Gender.not_given)
        self.assertEqual(gender_normalization("other gender"), Gender.other)

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
