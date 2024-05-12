class Car():
    def __init__(self, paint_color, year):
        self._paint_color = paint_color
        self._year = year
        self._mileage = 0.0
        self._oil_level = 0.0
        self._current_speed = 0.0
    
    def get_paint_color(self):
        return self._paint_color


if __name__ == '__main__':
    my_car = Car("Red", 2002)
    print("Car color:", my_car.get_paint_color())