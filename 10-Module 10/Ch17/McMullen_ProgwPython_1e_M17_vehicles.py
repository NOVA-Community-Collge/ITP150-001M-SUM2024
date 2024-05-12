class MotorVehicle():
    def __init__(self):
        self.make = ""
        self.model = ""
        self.color = ""
        self.vin = ""
        self.price = 0
        self.year = 0
        self.mileage = 0
        self.sold = False
        self.on_lot = True
    
    def give_discount(self, percentage):
        self.price -= self.price * percentage
    
    def increase_mileage(self, amount):
        self.mileage += amount
    
    def sell_vehicle(self, final_price):
        self.sold = True
        self.price = final_price
        
    def refuel(self, amount):
        self.fuel_level += amount
        if self.fuel_level > self.tank_capacity:
            self.fuel_level = self.tank_capacity

class GasVehicle(MotorVehicle):
    def __init__(self):
        super().__init__()
        self.mpg = 0
        self.fuel_level = 0.0
        self.tank_capacity = 0.0
    

class GasTruck(GasVehicle):
    def __init__(self):
        super().__init__()
        self.flatbed_length = 0.0
        self.flatbed_width = 0.0
            