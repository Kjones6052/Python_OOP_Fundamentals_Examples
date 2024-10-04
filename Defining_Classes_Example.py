class OfficeBuilding:
    def __init__(self, floors, offices):
        self.floors = floors
        self.offices = offices

    def open_doors(self):
        print("Doors are open for business!")

building1 = OfficeBuilding(10,200)
building2 = OfficeBuilding(20,400)
building1.open_doors()