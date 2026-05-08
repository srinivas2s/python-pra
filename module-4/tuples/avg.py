marks = (50, 60, 70, 80, 90)

avg = sum(marks)/len(marks)

above = []

for m in marks:
    if m > avg:
        above.append(m)

print("Average =", avg)
print("Count =", len(above))
print("Above Average =", above)