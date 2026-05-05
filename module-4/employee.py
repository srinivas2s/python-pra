employees = []

for i in range(3):
    name = input("Name: ")
    eid = int(input("EID: "))
    salary = float(input("Salary: "))
    employees.append((name, eid, salary))

print("\nEmployees:")
for emp in employees:
    print(emp)

highest = max(employees, key=lambda x: x[2])

print("\nHighest Salary Employee:")
print(highest)