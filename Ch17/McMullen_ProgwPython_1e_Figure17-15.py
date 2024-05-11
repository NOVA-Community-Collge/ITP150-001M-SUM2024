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

car = MotorVehicle()
car.make = "Temporary"
car.model = "Example"
car.color = "Blue"
car.vin = "ABC123"
car.price = 15000
car.year = 1980
print(car)
