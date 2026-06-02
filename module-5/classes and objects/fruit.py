class Fruit:
    def __init__(self, color):
        self.color = color

class Apple(Fruit):
    def __init__(self, color, taste):
        super().__init__(color)
        self.taste = taste

    def show(self):
        print("Apple Details")
        print("Color:", self.color)
        print("Taste:", self.taste)


class Mango(Fruit):
    def __init__(self, color, season, taste):
        super().__init__(color)
        self.season = season
        self.taste = taste

    def show(self):
        print("Mango Details")
        print("Color:", self.color)
        print("Taste:", self.taste)
        print("Season:", self.season)


# Creating objects
a1 = Apple("Red", "Sweet")
m1 = Mango("Yellow", "Summer", "Sweet")

# Displaying details
a1.show()
print()
m1.show()