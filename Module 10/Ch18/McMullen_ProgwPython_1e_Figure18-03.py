from vehicles import *
class Dealership():
    def __init__(self):
        self.owner = ""
        self.inventory = []
        self.address = ""
        self.capacity = 0
        
    def add_vehicle(self, motor_vehicle):
        if not isinstance(motor_vehicle, MotorVehicle):
            print("Can only add motor vehicle objects to a dealership.")
        elif len(self.inventory) < self.capacity:
            self.inventory.append(motor_vehicle)
        else:
            print("The lot is full. Cannot add vehicle.")
