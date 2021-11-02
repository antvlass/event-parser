from enum import Enum


def gender_normalization(text: str = None) -> str:
    if not text:
        return 'not_given'
    elif text.lower() in ["male", "female"]:
        return text.lower()
    else:
        return 'other'


class Gender(str, Enum):
    male = "male"
    female = "female"
    other = "other"
    not_given = "not_given"
