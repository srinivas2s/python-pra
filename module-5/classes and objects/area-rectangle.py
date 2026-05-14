class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)

    def display(self):
        print("\nRectangle Details")
        print("Length =", self.length)
        print("Breadth =", self.breadth)
        print("Area =", self.area())
        print("Perimeter =", self.perimeter())

length = float(input("Enter length: "))
breadth = float(input("Enter breadth: "))
r1 = Rectangle(length, breadth)
r1.display()

