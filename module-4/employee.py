employees = []
for i in range(3):
    name = input("Enter Name: ")
    eid = int(input("Enter Employee ID: "))
    salary = float(input("Enter Salary: "))
    employees.append((name, eid, salary))
print("\nEmployee Records")
for emp in employees:
    print(emp)
highest = employees[0]
for emp in employees:
    if emp[2] > highest[2]:
        highest = emp
print("\nEmployee with Highest Salary:")
print(highest)
