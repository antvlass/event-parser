from unittest import TestCase

from event_parser.gender import Gender
from event_parser.person import Person


class TestPerson(TestCase):
    def test_first_name(self):
        person = Person(
            first_name="Tom",
            last_name="Sawyer",
            gender=Gender.male,
            email="tom.sawyer@mail.com"
        )
        self.assertEqual(person.first_name, "Tom")

    def test_last_name(self):
        person = Person(
            first_name="Tom",
            last_name="Sawyer",
            gender=Gender.male,
            email="tom.sawyer@mail.com"
        )
        self.assertEqual(person.last_name, "Sawyer")
