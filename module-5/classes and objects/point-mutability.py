class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

p1 = Point(10,20)

print("Before modification:")
print("x =", p1.x)
print("y =", p1.y)

p1.x = p1.x + 10
p1.y = p1.y + 20

print("\nAfter modification:")
print("x =", p1.x)
print("y =", p1.y)
