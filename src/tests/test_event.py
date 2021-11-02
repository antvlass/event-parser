from unittest import TestCase
from ipaddress import IPv4Address

from event_parser.event import ip_anonymization


class TestEvent(TestCase):
    def test_ip_anonymization(self):
        self.assertEqual(ip_anonymization(IPv4Address(
            "10.171.57.131")), IPv4Address("10.171.57.0"))
        self.assertEqual(ip_anonymization(IPv4Address(
            "86.69.117.124")), IPv4Address("86.69.117.0"))
        self.assertEqual(ip_anonymization(IPv4Address(
            "110.184.3.0")), IPv4Address("110.184.3.0"))
