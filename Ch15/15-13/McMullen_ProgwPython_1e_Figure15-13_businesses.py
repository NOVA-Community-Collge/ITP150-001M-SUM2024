class Dealership():
    def __init__(self):
        self.owner = ""
        self.inventory = []
        self.address = ""
        
    def add_car(self, car):
        if len(self.inventory) < self.capacity:
            self.inventory.append(car)
        else:
            print("The lot is full. Cannot add car.")
    
    def sell_car(self, car, final_price):
        pass
    
    def test_drive(self, car, license_number):
        pass
    
    def check_in_car(self, car, services):
        pass