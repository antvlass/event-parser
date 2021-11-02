from unittest import TestCase
from event_parser.gender import gender_normalization


class TestGender(TestCase):
    def test_gender_normalization(self):
        self.assertEqual(gender_normalization("Female"), "female")
        self.assertEqual(gender_normalization("MALE"), "male")
        self.assertEqual(gender_normalization(None), "not_given")
        self.assertEqual(gender_normalization("other gender"), "other")
