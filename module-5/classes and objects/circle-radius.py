class Circle:
    def __init__(self, radius):
        self.radius = radius

    def display(self):
        print("Radius =", self.radius)

def double_radius(circle):
    return Circle(circle.radius * 2)

r = float(input("Enter the radius: "))
c1 = Circle(r)
c2 = double_radius(c1)

print("\nOriginal Circle:")
c1.display()
print("\nNew Circle with Doubled Radius:")
c2.display()
