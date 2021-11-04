from typing import List
import csv
from ipaddress import IPv4Address

from event_parser.event import Event
from event_parser.gender import Gender
from event_parser.person import Person


def ip_anonymization(ip: IPv4Address) -> IPv4Address:
    '''
    This function will anonymize a given IPV4 adress by setting the last byte to 0.
    In this way, most of the information is preserved but cannot be linked to an 
    individual person.
    Input: IPv4 adress to anonymize
    Output: Anonymized IPv4 adress
    '''
    # Conversion of the IP to its string format
    ip_bytes = ip.exploded.split('.')
    # Put the last byte to 0
    ip_bytes[-1] = '0'
    # Reform the IPv4 adress
    return IPv4Address('.'.join(ip_bytes))


def gender_normalization(text: str = None) -> Gender:
    '''
    This function will normalize an input text to match a
    specific Gender category.
    Input: Data text
    Output: Gender category
    '''
    if not text:
        return Gender.not_given
    elif text.lower() in ["male", "female"]:
        return getattr(Gender, text.lower())
    else:
        return Gender.other


def read_events(path: str) -> List[Event]:
    '''
    This function will read and parse a csv file as a list
    of Event objects
    Input: path to csv file
    Output: list of Event objects
    '''
    events = list()
    with open(path) as data_file:
        data = csv.reader(data_file)
        next(data)  # skip the header
        for row in data:
            person = Person(
                first_name=row[1],
                last_name=row[2],
                gender=gender_normalization(row[4]),
                email=row[3]
            )
            events.append(Event(id=row[0], person=person, ip_adress=row[5]))
    return events
