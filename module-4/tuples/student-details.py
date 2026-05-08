students = []

n = int(input("Number of students: "))

for i in range(n):
    usn = input("USN: ")
    name = input("Name: ")
    marks = int(input("Marks: "))

    students.append((usn, name, marks))

print("\nRecords:")
for s in students:
    print(s)

highest = max(students, key=lambda x: x[2])

print("\nHighest Scorer:")
print(highest)