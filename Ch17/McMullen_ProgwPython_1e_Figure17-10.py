from vehicles import GasTruck  

t = GasTruck()
t.make = "Nissan"
t.model = "Frontier"
t.color = "Blue"
t.vin = "DEF1234567"
t.price = 19290
t.mpg = 25
t.year = 2020
t.mileage = 1000
t.fuel_level = 20.0
t.tank_capacity = 21.1
t.flatbed_length = 9.1
t.flatbed_width = 5.25

print("Truck features:")
print("Make:", t.make)
print("Model:", t.model)
print("Color:", t.color)
print("Year:", t.year)
print("Price:", t.price)
print("Flatbed Length:", t.flatbed_length)
print("Flatbed Width:", t.flatbed_width)
