# Omitted in the figure
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
        raise NotImplementedError("Child classes of MotorVehicle must implement a refueling method.")
        
    def __str__(self):
        result = ""
        result += "{:>10s}: {:s}\n".format("Make", self.make)
        result += "{:>10s}: {:s}\n".format("Model", self.model)
        result += "{:>10s}: {:s}\n".format("Color", self.color)
        result += "{:>10s}: {:s}\n".format("VIN", self.vin)
        result += "{:>10s}: ${:0.2f}\n".format("Price", self.price)
        result += "{:>10s}: {:d}\n".format("Year", self.year)
        result += "{:>10s}: {:d}\n".format("Mileage", self.mileage)
        result += "{:>10s}: {:s}\n".format("Sold", str(self.sold))
        result += "{:>10s}: {:s}\n".format("On Lot", str(self.on_lot))
        return result
# End omission

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
    
    def __str__(self):
        result = super().__str__()
        result += "{:>10s}: {:.2f}\n".format("Fuel Level", self.fuel_level)
        result += "{:>10s}: {:.2f}\n".format("Tank Cap", self.tank_capacity)
        return result

class ElectricVehicle(MotorVehicle):
    def __init__(self):
        super().__init__()
        self.mpge = 0 # Miles Per Gallon Equivalent
        self.battery_percent = 0.0
    
    def refuel(self, amount):
        self.battery_percent += amount
        if self.battery_percent > 100:
            self.battery_percent = 100.0

    def __str__(self):
        result = super().__str__()
        result += "{:>10s}: %{:.2f}\n".format("Battery", self.battery_percent)
        return result
