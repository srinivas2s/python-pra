class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"Employee ID: {self.emp_id}, Name: {self.name}, Salary: {self.salary}"
e1 = Employee(101, "John", 50000)
e2 = Employee(102, "Mary", 60000)
e3 = Employee(103, "David", 55000)

print(e1)
print(e2)
print(e3)
