gas_car = GasVehicle()
gas_car.make = "Honda"
gas_car.model = "Fit"
gas_car.color = "Gray"
gas_car.vin = "ABC123"
gas_car.price = 15000
gas_car.year = 2014
gas_car.tank_capacity = 10
gas_car.refuel(6)

electric_car = ElectricVehicle()
electric_car.make = "Tesla"
electric_car.model = "Model 3"
electric_car.color = "Green"
electric_car.vin = "DEF456"
electric_car.price = 30000
electric_car.year = 2018
electric_car.refuel(87)

print(gas_car)
print(electric_car)
