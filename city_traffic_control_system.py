from vehicle import Vehicle
from traffic_signal import TrafficSignal

intersection = TrafficSignal()
vehicles = []

while True:
    action = input("Enter action (add, signal, display, exit): ")
    if action == "exit":
        break

    try:
        if action == "add":
            vehicle_type = input("Enter vehicle type: ")
            vehicles.append(Vehicle(vehicle_type))
            print(f"Added {vehicle_type}.")
        elif action == "signal":
            intersection.change_signal()
            if intersection.current_signal == "green":
                vehicles.clear()
                print("Intersection cleared.")
            intersection.display_signal()
        elif action == "display":
            print(f"Signal: {intersection.current_signal}")
            for vehicle in vehicles:
                vehicle.display_type()
    except Exception as e:
        print(f"An error occurred: {e}")

print("Traffic control system closed.")