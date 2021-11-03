import sys
from event_parser.reader import read_events
from event_parser.event import ip_anonymization
from event_parser.gender import Gender


def main(path: str) -> None:
    events = read_events(path)
    # 1. Count the number of females and print the answer
    events_females = [
        event for event in events if event.person.gender == Gender.female]
    print("1. There are {} females in the dataset".format(len(events_females)))

    # 2. Count the number of females starting with letter "A" and print the answer
    starts_a = [
        event for event in events_females if event.person.first_name[0].lower() == 'a']
    print("2. There are {} females starting with the letter 'A' in the dataset".format(
        len(starts_a)))

    # 3. Count the number of distinct first names and print the answer
    unique_firstnames = set(map(lambda x: x.person.first_name, events))
    print("3. There are {} unique first names in the dataset".format(
        len(unique_firstnames)))

    # 4. Count the number of unique IP addresses and print the answer
    unique_ip = set(map(lambda x: x.ip_adress, events))
    print("4. There are {} unique IP adresses in the dataset".format(len(unique_ip)))

    # 5. Implement an IP anonymization function, and print the first 10 IP addresses in an anonymized form; describe your approach in comments
    print("5. The first 10 IPs in an anonymized form:")
    for i in range(10):
        print(ip_anonymization(events[i].ip_adress))

    # 6. There is at least one duplicate event ID; print out the number of event IDs that have at least one occurrence in the dataset
    # equilavent in finding the unique count of IDs
    unique_id = set(map(lambda x: x.id, events))
    print("6. There are {} event IDs with at least one occurrence in the dataset".format(
        len(unique_id)))


if __name__ == "__main__":
    path = sys.argv[1]
    main(path)
