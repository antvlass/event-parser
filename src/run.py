import sys

from event_parser.reader import read_events


def main(path: str) -> None:
    events = read_events(path)

    ### 1. Count the number of females and print the answer

    ### 2. Count the number of females starting with letter "A" and print the answer

    ### 3. Count the number of distinct first names and print the answer

    ### 4. Count the number of unique IP addresses and print the answer

    ### 5. Implement an IP anonymization function, and print the first 10 IP addresses in an anonymized form; describe your approach in comments

    ### 6. There is at least one duplicate event ID; print out the number of event IDs that have at least one occurrence in the dataset

if __name__ == "__main__":
    path = sys.argv[1]   
    main(path)