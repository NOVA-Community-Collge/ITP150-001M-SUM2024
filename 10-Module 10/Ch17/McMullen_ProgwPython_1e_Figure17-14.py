class GasVehicle(MotorVehicle):
    def __init__(self):
        super().__init__()       
        self.mpg = 0 
        self.fuel_level = 0.0
        self.tank_capacity = 0.0
        
    def refuel(self, amount):
        self.fuel_level += amount
        if self.fuel_level > self.tank_capacity:
            self.fuel_level = self.tank_capacity

class ElectricVehicle(MotorVehicle):
    def __init__(self):
        super().__init__()
        self.mpge = 0 # Miles Per Gallon Equivalent
        self.battery_percent = 0.0
    
    def refuel(self, amount):
        self.battery_percent += amount
        if self.battery_percent > 100:
            self.battery_percent = 100.0

class HybridVehicle(GasVehicle, ElectricVehicle):
    def __init__(self):
        super().__init__()
    
    def refuel(self, amount, fuel_type):
        if fuel_type == "gas":
            GasVehicle.refuel(self, amount)
        else:
            ElectricVehicle.refuel(self, amount)
