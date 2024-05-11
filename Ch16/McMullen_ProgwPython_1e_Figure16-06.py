from vehicle import Car

def accelerate(car, amount):
    car.current_speed += amount


my_car = Car()
accelerate(my_car, 50)
print("Current speed:", my_car.current_speed, "MPH.")