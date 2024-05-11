from businesses import Dealership
from vehicle import Car
import random
import string

dealer = Dealership()
dealer.capacity = 20

make_and_model_options = [["Honda", "Fit"], ["Toyota", "Celica"], ["Ford", "F150"]]
colors = ["Blue", "Green", "Gray", "Black", "White", "Red"]

# Add 10 random cars
for i in range(10):
    car = Car()
    car.make, car.model = random.choice(make_and_model_options)
    car.year = random.randint(2009, 2010)
    car.color = random.choice(colors)
    car.vin = "".join(random.choices(string.ascii_uppercase, k=3)) + "".join(random.choices("0123456789",k=5))
    car.price = random.randint(15000,200000)
    car.mpg = random.randint(15,50)
    car.on_lot = True
    
    dealer.add_car(car)

search_car = Car()
search_car.make = "Toyota"
search_car.model = "Celica"
search_car.color = "Blue"
search_car.year = 2009

print("You are looking for a", search_car.color,
      search_car.make, search_car.model, "from", str(search_car.year) + ".")

is_car_available = False

for car_on_lot in dealer.inventory:
    if car_on_lot == search_car:
        is_car_available = True
        break
    
if is_car_available:
    print("We have that car for sale!")
else:
    print("We don't have that car for sale, sorry!")
        

