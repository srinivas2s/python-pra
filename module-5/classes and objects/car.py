class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display(self):
        print("\nCar Details")
        print("Brand :", self.brand)
        print("Model :", self.model)

brand = input("Enter car brand: ")
model = input("Enter car model: ")

c1 = Car(brand, model)

c1.display()
