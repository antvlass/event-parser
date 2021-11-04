from pydantic import BaseModel, Field

from event_parser.person import Person
from ipaddress import IPv4Address

# The `Event` class should completely encapsulate an event as per `events.csv` file


class Event(BaseModel):
    id: int = Field(...)
    person: Person
    ip_adress: IPv4Address = Field(...)
