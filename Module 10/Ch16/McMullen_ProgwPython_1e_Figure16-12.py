AVAILABLE_COLORS = ["Blue", "Red", "Green", "Black", "White", "Gray"]

class Car():
    def __init__(self, paint_color="Black", year=1908):
        self.set_paint_color(paint_color)
        self.set_year(year)
        self._mileage = 0.0
        self._oil_level = 0.0
        self._current_speed = 0.0
    
    def set_paint_color(self, paint_color):
        # See if the color is in the AVAILABLE_COLORS list
        for color in AVAILABLE_COLORS :
            if color == paint_color:
                # If the color is in the list, then it’s valid
                self._paint_color = paint_color
                return
        # If the code reaches this point, it is not a valid color
        # Defaults to the first color in the AVAILABLE_COLORS list
        self._paint_color = AVAILABLE_COLORS[0]
    
    def set_year(self, year):
        if year >= 1908:
            self._year = year
        else:
            self._year = 1908
            
