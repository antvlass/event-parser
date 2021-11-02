from typing import List
import csv

from event_parser.event import Event
from event_parser.gender import Gender, gender_normalization
from event_parser.person import Person


def read_events(path: str) -> List[Event]:
    events = list()
    with open(path) as data_file:
        data = csv.reader(data_file)
        # skip the header
        next(data)
        for row in data:
            person = Person(
                first_name=row[1],
                last_name=row[2],
                gender=getattr(Gender, gender_normalization(row[4])),
                email=row[3]
            )
            events.append(Event(id=row[0], person=person, ip_adress=row[5]))
    return events
