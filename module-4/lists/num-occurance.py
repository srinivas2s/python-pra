file = open("input.txt", "r")
data = file.read()
file.close()

digits = set()
special = {}

for ch in data:
    if ch.isdigit():
        digits.add(ch)

    elif not ch.isalnum() and not ch.isspace():
        special[ch] = special.get(ch, 0) + 1

print("Unique Digits Count =", len(digits))
print("Digits =", digits)
print("Special Characters =", special)