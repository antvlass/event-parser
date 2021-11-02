from pydantic import BaseModel, Field

from event_parser.gender import Gender


class Person(BaseModel):
    first_name: str = Field(...)
    last_name: str = Field(...)
    gender: Gender
    email: str = Field(...)