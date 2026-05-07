data = ('A','11','B1','23','44','ACB13')

digits = ()
alpha = ()

for x in data:
    if x.isdigit():
        digits += (x,)
    else:
        alpha += (x,)

s = ""

for x in data:
    s += x

print("Digits =", digits)
print("Alphanumeric =", alpha)
print("String =", s)
print("Length =", len(s))