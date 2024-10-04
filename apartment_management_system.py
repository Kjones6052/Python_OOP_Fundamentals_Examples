class ApartmentBuilding:
    shared_facilities = ['Gym', 'Swimming Pool', 'Parking Lot']

    def __init__(self, name, total_units):
        self.name = name
        self.total_units = total_units
        self.occupied_units = 0

    def update_occupancy(self, change):
        if 0 <= self.occupied_units + change <= self.total_units:
            self.occupied_units += change
            return True
        return False
    
    def available_units(self):
        return self.total_units - self.occupied_units
    
    def occupancy_rate(self):
        return (self.occupied_units / self.total_units) * 100

buildings = []

while True:
    action = input("Enter action (add, update, list, exit): ").lower()
    if action == "exit":
        break

    try:
        if action == "add":
            name = input("Enter building name: ")
            units = int(input("Enter total units: "))
            buildings.append(ApartmentBuilding(name, units))
            print(f"Building '{name}' added with {units} units.")
        elif action == "update":
            name = input("Enter building name: ")
            change = int(input("Enter change in occupied units: "))
            for building in buildings:
                if building.name == name:
                    if building.update_occupancy(change):
                        print(f"Updated occupancy for '{name}'.")
                    else:
                        print("Invalid occupancy change.")
                        break
            else:
                print("Building not found.")
        elif action == "list":
            for building in buildings:
                print(f"{building.name}: {building.available_units()} available units, "
                      f"Occupancy rate: {building.occupancy_rate():.2f}%")
                
        else:
            print("Building not found.")
    except ValueError:
        print("Invalid input, please enter numeric values for units.")
    except Exception as e:
        print(f"An error occurred: {e}")