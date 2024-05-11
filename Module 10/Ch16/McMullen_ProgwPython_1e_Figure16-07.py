class Car():
    def __init__(self):
        self.paint_color = ""
        self.year = 0
        self.mileage = 0.0
        self.oil_level = 0.0
        self.current_speed = 0.0
    
    def should_change_oil(self):
        return self.oil_level < 0.5
    
    def accelerate(self, amount):
        self.current_speed += amount


if __name__ == '__main__':        
    my_car = Car()
    my_car.accelerate(50)
    print("Current speed:", my_car.current_speed, "MPH.")