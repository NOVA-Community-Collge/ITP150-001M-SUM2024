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
    
    def calculate_fuel_consumption(self, miles):
        raise NotImplementedError("All child classes of MotorVehicle must implement calculate_fuel_consumption.")
    
    # Other methods omitted

class GasVehicle(MotorVehicle):
    def __init__(self):
        super().__init__()       
        self.mpg = 0 
        self.fuel_level = 0.0
        self.tank_capacity = 0.0
        
    def calculate_fuel_consumption(self, miles):
        return self.mpg * miles
    
    # Other methods omitted

class ElectricVehicle(MotorVehicle):
    def __init__(self):
        super().__init__()
        self.battery_percent = 0.0
        self.electricity_cost = 0.0
    
    def calculate_fuel_consumption(self, miles):
        return self.electricity_cost * miles
    
    # Other methods omitted

class HybridVehicle(GasVehicle, ElectricVehicle):
    def __init__(self):
        super().__init__()
        self.battery_savings_per_mile = 0.0
    
    def calculate_fuel_consumption(self, miles):
        return self.mpg * miles - self.battery_savings_per_mile * miles
    
    # Other methods omitted
    

tesla = ElectricVehicle()
tesla.electricity_cost = 13.0
honda = GasVehicle()
honda.mpg = 30.0
prius = HybridVehicle()
prius.battery_savings_per_mile = 4.0
prius.mpg = 25.0

print("Fuel consumption for 10 miles")
print("Tesla:", tesla.calculate_fuel_consumption(10))
print("Honda:", honda.calculate_fuel_consumption(10))
print("Prius:", prius.calculate_fuel_consumption(10))
