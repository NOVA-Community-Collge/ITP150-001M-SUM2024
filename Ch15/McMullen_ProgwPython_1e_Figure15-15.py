class Car():
    def __init__(self, make, model, color, year, vin="", price=0, mpg=0):
        self.make = make
        self.model = model
        self.color = color
        self.vin = vin
        self.price = price
        self.mpg = mpg
        self.year = year
        self.mileage = 0
        self.sold = False
        self.on_lot = True
    
    def clone(self):
        cloned_car = Car(self.make, self.model, self.color,
                         self.year, self.vin, self.price, self.mpg)
        
        return cloned_car
        
    def __eq__(self, other):
        if self.make == other.make and  \
           self.model == other.model and \
           self.color == other.color and \
           self.year == other.year:
            return True
        
        else:
            return False
    
    def __str__(self):
        string = "Make: " + self.make + "\n"
        string += "Model: " + self.model + "\n"
        string += "Color: " + self.color + "\n"
        string += "Vin: " + self.vin + "\n"
        string += "Price: " + str(self.price) + "\n"
        string += "MPG: " + str(self.mpg) + "\n"
        string += "Year: " + str(self.year) + "\n"
        string += "Mileage: " + str(self.mileage) + "\n"
        string += "Is Sold: " + str(self.sold) + "\n"
        string += "Is On Lot: " + str(self.on_lot) + "\n"
        
        return string