from pydantic import BaseModel, Field

from event_parser.person import Person
from ipaddress import IPv4Address

# The `Event` class should completely encapsulate an event as per `events.csv` file


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


class Event(BaseModel):
    id: int = Field(...)
    person: Person
    ip_adress: IPv4Address = Field(...)
