from event_manager import Event
import os

events = []

def save_events_to_file():
    with open('events.txt', 'w') as file:
        for event in events.values():
            file.write(f"{event.name}, {event.date}, {event.location}, {', '.join(event.participants)}\n")

def load_events_from_file():
    if os.path.exists('events.txt'):
        with open('events.txt', 'r') as file:
            for line in file:
                name, date, location, *participants = line.strip().split(',')
                event = event(name, date, location)
                event.participants = participants
                events[name] = event

load_events_from_file()

while True:
    action = input("Enter action (add, register, display, save, exit): ").lower()
    if action == "exit":
        break

    try:
        if action == "add":
            name = input("Enter event name: ")
            date = input("Enter event date: ")
            location = input("Enter event location: ")
            events[name] = (Event(name, date, location))
        elif action == "register":
            event_name = input("Enter event name: ")
            participant = input("Evnter participant name: ")
            if event_name in events:
                events[event_name].register_participant(participant)
            else:
                print("Event not found.")
        elif action == "display":
            for event in events.values():
                event.display_event()
        elif action == "save":
            save_events_to_file()
            print("Events saved to file.")
    except Exception as e:
        print(f"An error occurred: ")

print("Event Planner System Closed.")