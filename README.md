# Event Parser (Take-Home Assignment)

## Description

In this task you are supposed to complete the event parsing code, and perform some basic analytics on a sample dataset. More specifically,
you are supposed to complete `src/event_parser/event.py`, `src/event_parser/reader.py`, and `src/run.py`, and ensure adequate test coverage 
in `src/tests/`, which will be run with `pytest`. The sample dataset is provided in a CSV file `data/events.csv`.

Besides testing your problem solving skills, this task is intended to test your software craftsmanship skills, adherence to style, consistency, etc.

__Bonus:__ As a bonus exercise, provide the answer to the supplied question in the file `BONUS.txt`.

## Pre-Requisites

* Python 3.6+
* [Poetry](https://python-poetry.org)

Once the above pre-requisites are met, initialize your Python environment as follows:

```
poetry install
poetry shell
```

## Completion Requirements

For the assignment to be considered successfully completed, the following requirements need to be met:

* All marked sections completed
* All counting/analytics functions implemented and yield correct results
* Adequate test coverage implemented and all tests passed
* Use type hints in function definitions
* You are not allowed to use any other libs/dependencies than what is already provided in `pyproject.toml`
* For naming, imports, etc, you should adhere to PEP-8 style guide

## Tips/Hints

* Text normalization is generally a good idea, especially when it comes to categorical variables!

## References/Links:

* Pydantic: https://pydantic-docs.helpmanual.io
* PEP-8: https://www.python.org/dev/peps/pep-0008/