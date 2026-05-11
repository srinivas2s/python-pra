f = open("file.txt", "r")
data = f.read()
f.close()
count = 0
for ch in data:
    if ch != ' ':
        count += 1

print("Number of characters (excluding spaces):", count)

digit_list = []
for i in range(len(data)):
    if data[i].isdigit():
        digit_list.append((data[i], i))
print("Digits with index values:")
print(digit_list)
