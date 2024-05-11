class Car_Interface():
    
    # Accessors
    def get_year(self):
        raise NotImplementedError("get_year must be implemented.")
    def get_paint_color(self):
        raise NotImplementedError("get_paint_color must be implemented.")
    def get_mileage(self):
        raise NotImplementedError("get_mileage must be implemented.")
    def get_speed(self):
        raise NotImplementedError("get_speed must be implemented.")
    def should_change_oil(self):
        raise NotImplementedError("should_change_oil must be implemented.")
    
    # Mutators
    def set_paint_color(self, paint_color):
        raise NotImplementedError("set_paint_color must be implemented.")    
    def set_year(self, year):
        raise NotImplementedError("set_year must be implemented.")
    def increase_miles(self, amount):
        raise NotImplementedError("increase_miles must be implemented.")
    def accelerate(self, amount):
        raise NotImplementedError("accelerate must be implemented.")
    def travel(self, time_in_seconds):
        raise NotImplementedError("travel must be implemented.")
