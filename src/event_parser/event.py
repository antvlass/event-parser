from pydantic import BaseModel, Field

from event_parser.person import Person


# The `Event` class should completely encapsulate an event as per `events.csv` file

class Event(BaseModel):
    ### INSERT HERE ###