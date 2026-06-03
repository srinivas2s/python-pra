class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def fuel_type(self):
        print("Fuel type not specified")

class FourWheeler(Vehicle):
    def fuel_type(self):
        print("Fuel type: Petrol/Diesel")

class TwoWheeler(Vehicle):
    def fuel_type(self):
        print("Fuel type: Petrol/Electric")

v1 = FourWheeler("Toyota", "Fortuner", 2023)
v2 = TwoWheeler("Yamaha", "R15", 2022)

for v in (v1, v2):
    print(f"{v.brand} {v.model} ({v.year})")
    v.fuel_type()
    print()


