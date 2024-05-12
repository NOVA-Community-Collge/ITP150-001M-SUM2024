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
        

