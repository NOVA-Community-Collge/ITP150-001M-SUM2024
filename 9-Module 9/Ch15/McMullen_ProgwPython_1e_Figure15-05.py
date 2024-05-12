from businesses import Dealership
from vehicle import Car

dealer = Dealership()
dealer.owner = input("What is your name? ")
dealer.address = input("What is your address? ")
dealer.capacity = int(input("What is your lot's capacity? "))

num_new_cars = int(input("How many cars would you like to enter? "))

for i in range(num_new_cars):
    new_car = Car()
    new_car.make = input("Please enter the car's make: ")
    new_car.model = input("Please enter the car's model: ")
    new_car.color = input("Please enter the car's color: ")
    new_car.vin = input("Please enter the car's vin: ")
    new_car.price = float(input("Please enter the car's price: "))
    new_car.mpg = float(input("Please enter the car's mpg: "))
    new_car.year = int(input("Please enter the car's year: "))
    new_car.mileage = int(input("Please enter the car's mileage: "))
    
    print()

    dealer.add_car(new_car)
