class Car():
    def __init__(self):
        self.make = ""
        self.model = ""
        self.color = ""
        self.vin = ""
        self.price = 0
        self.mpg = 0
        self.year = 0
        self.mileage = 0
        self.sold = False
        self.on_lot = False
        
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
        