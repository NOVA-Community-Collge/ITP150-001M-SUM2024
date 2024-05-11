AVAILABLE_COLORS = ["Blue", "Red", "Green", "Black", "White", "Gray"]

class Car():
    def __init__(self, paint_color, year):
        self.set_paint_color(paint_color)
        self.set_year(year)
        self._mileage = 0.0
        self._oil_level = 0.0
        self._current_speed = 0.0
    
    def set_paint_color(self, paint_color):
        for color in AVAILABLE_COLORS:
            if color == paint_color:
                self._paint_color = paint_color
                return
        self._paint_color = AVAILABLE_COLORS[0]
    
    def set_year(self, year):
        if year >= 1908:
            self._year = year
        else:
            self._year = 1908
            
