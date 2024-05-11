class Car():
    def __init__(self, make, model, color, year, vin="", price=0, mpg=0):
        self._make = make
        self._model = model
        self._color = color
        self._vin = vin
        self._price = price
        self._mpg = mpg
        self._year = year
        self._mileage = 0
        self._sold = False
        self._on_lot = True
    
    def get_make(self):
        return self._make    
    def get_model(self):
        return self._model    
    def get_color(self):
        return self._color    
    def get_vin(self):
        return self._vin    
    def get_price(self):
        return self._price    
    def get_mpg(self):
        return self._mpg
    def get_year(self):
        return self._year
    def get_mileage(self):
        return self._mileage
    def is_sold(self):
        return self._sold
    def is_on_lot(self):
        return self._on_lot
        
    def __eq__(self, other):
        if self._make == other.make and \
           self._model == other.model and \
           self._color == other.color and \
           self._year == other.year:
            return True
        
        else:
            return False
    
    def __str__(self):
        string = "Make: " + self._make + "\n"
        string += "Model: " + self._model + "\n"
        string += "Color: " + self._color + "\n"
        string += "Vin: " + self._vin + "\n"
        string += "Price: " + str(self._price) + "\n"
        string += "MPG: " + str(self._mpg) + "\n"
        string += "Year: " + str(self._year) + "\n"
        string += "Mileage: " + str(self._mileage) + "\n"
        string += "Is Sold: " + str(self._sold) + "\n"
        string += "Is On Lot: " + str(self._on_lot) + "\n"
        
        return string
