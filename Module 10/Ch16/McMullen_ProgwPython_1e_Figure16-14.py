from interfaces import Car_Interface

class Car(Car_Interface):
    def __init__(self):
        self.paint_color = ""
        self.year = 0
        self.mileage = 0.0
        self.oil_level = 0.0
        self.current_speed = 0.0        
        
    def set_year(self, year):
        if year >= 1908:
            self._year = year
        else:
            self._year = 1908
    
    # Implementation of all methods from the
    # interface omitted
    