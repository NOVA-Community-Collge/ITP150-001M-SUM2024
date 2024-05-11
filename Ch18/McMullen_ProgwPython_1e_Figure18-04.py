from businesses import Dealership
from vehicles import *

zoes_zippy_cars = Dealership()
zoes_zippy_cars.capacity = 100
# Other code to initialize properties of the Dealership

corolla = GasVehicle()
tesla = ElectricVehicle()
prius = HybridVehicle()

zoes_zippy_cars.add_vehicle(corolla)
zoes_zippy_cars.add_vehicle(tesla)
zoes_zippy_cars.add_vehicle(prius)

print("Total vehicles on lot:", len(zoes_zippy_cars.inventory))