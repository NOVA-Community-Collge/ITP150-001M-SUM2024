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
    make, model = random.choice(make_and_model_options)
    dealer.add_car(Car(make, model, random.choice(colors),
                       random.randint(2009, 2010),
                       "".join(random.choices(string.ascii_uppercase, k=3)) + "".join(random.choices("0123456789",k=5)),
                       random.randint(15000,200000),
                       random.randint(15,50)))

search_car = Car("Toyota", "Celica", "Blue", 2009, "", 0, 0)

print("You are looking for a", search_car.color,
      search_car.make, search_car.model, "from", str(search_car.year) + ".")
print()

is_car_available = False

for car_on_lot in dealer.inventory:
    if car_on_lot == search_car:
        is_car_available = True
        break
    
if is_car_available:
    print("We have that car for sale!")
else:
    print("We don't have that car for sale, sorry!")
        

