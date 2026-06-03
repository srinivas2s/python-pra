class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def display(self):
        print(self.x,",",self.y)

v1 = Vector(2, 3)
v2 = Vector(4, 5)

v3 = v1 + v2
print("Vector 1 =")
v1.display()
print("Vector 2 =")
v2.display()
print("Sum of Vectors =")
v3.display()
