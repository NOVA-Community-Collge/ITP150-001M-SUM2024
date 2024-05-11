class GasVehicle(MotorVehicle):
    def __init__(self):
        super().__init__()
        self.mpg = 0
    

class GasTruck(GasVehicle):
    def __init__(self):
        super().__init__()
        self.flatbed_length = 0.0
        self.flatbed_width = 0.0
            
