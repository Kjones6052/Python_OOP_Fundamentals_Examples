
class Vehicle:
    def __init__(self, reg_num, vehicle_typle, owner):
        self.reg_num = reg_num
        self.vehicle_type = vehicle_typle
        self.owner = owner

    def update_owner(self, new_owner):
        self.owner = new_owner

    def display_details(self):
        print(f"Registration: {self.reg_num}, Type: {self.vehicle_type}, Owner: {self.owner}")

vehicles = []

def register_vehicle(reg_num, vehicle_type, owner):
    if reg_num in vehicles:
        print("Error: Registration number already exists.")
        return
    vehicles[reg_num] = Vehicle(reg_num, vehicle_type, owner)
    print(f"Vehicle with reg num {reg_num} registered.")

def update_vehicle_owner(reg_num, new_owner):
    if reg_num in vehicles:
        vehicles[reg_num].update_owner(new_owner)
        print(f"Updated owner for vehicle: {reg_num}")
    else:
        print("Vehicle not found.")

def display_vehicles():
    for vehicle in vehicles.values():
        vehicle.display_details()