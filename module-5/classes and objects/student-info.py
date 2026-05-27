class Student:
    def __init__(self, name, age, m1, m2, m3):
        self.name = name
        self.age = age
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def display(self):
        print("\nStudent Details")
        print("Name :", self.name)
        print("Age :", self.age)
        print("Marks in Subject 1 :", self.m1)
        print("Marks in Subject 2 :", self.m2)
        print("Marks in Subject 3 :", self.m3)
# Input from user
name = input("Enter student name: ")
age = int(input("Enter age: "))
m1 = int(input("Enter marks in Subject 1: "))
m2 = int(input("Enter marks in Subject 2: "))
m3 = int(input("Enter marks in Subject 3: "))
# Creating object
s1 = Student(name, age, m1, m2, m3)
s1.display()