def result(marks):
    mn = min(marks)
    mx = max(marks)
    return mn, mx

marks = (56, 78, 90, 45, 67)

mn, mx = result(marks)

print("Minimum:", mn)
print("Maximum:", mx)