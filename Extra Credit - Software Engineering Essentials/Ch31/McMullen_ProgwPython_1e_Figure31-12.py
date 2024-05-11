class Teapot():

    def __init__(self, color):
        self._color = color
        self._temperature = 0
        self._water_amount = 0
        self._tea_type = "Green"
        
    def heat_up(self, temperature):
        self._temperature = temperature

    def add_water(self, amount):
        self._water_amount += amount

    def change_tea(self, tea):
        self._tea_type = tea

    def pour(self, amount):
        self._water_amount -= amount
    
    def __str__(self):
        string = "Teapot status:\n"
        string += "Color: " + t._color + "\n"
        string += "Temperature: " + str(self._temperature) + "\n"
        string += "Tea Type: " + self._tea_type + "\n"
        string += "Water Amount: " + str(self._water_amount) + "\n"
        
        return string

if __name__ == '__main__':
    t = Teapot("Blue")
    t.change_tea("Oolong")
    t.add_water(25.5)
    t.heat_up(95)
    t.pour(2.75)
    
    print(t)
    

