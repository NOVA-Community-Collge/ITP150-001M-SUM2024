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
        
    # Mutators
    def set_make(self, make):
        self._make = make    
    def set_model(self, model):
        self._model = model    
    def set_color(self, color):
        self._color = color   
    def set_vin(self, vin):
        self._vin = vin   
    def set_price(self, price):
        if price > 0:
           self._price = price  
    def set_mpg(self, mpg):
        if price > 0:
            self._mpg = mpg
    def set_year(self, year):
        if year > 1908:
            self._year = year
    def set_mileage(self, mileage):
        if mileage > 0:
            self._mileage = mileage
    def sell(self):
        self._sold = True
    def leave_lot(self):
        self._on_lot = False
    def return_to_lot(self):
        self._on_lot = True
        
    # Accessors
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
