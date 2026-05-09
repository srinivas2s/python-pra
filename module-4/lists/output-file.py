
file = open("ip.txt", "r")
data = file.read()
lines = data.split('\n')
file.close()


outfile = open("output.txt", "w")
for i in range(len(lines)):
    if i % 2 == 0:
        outfile.write(lines[i] + '\n')
outfile.close()
print("Odd-numbered lines copied successfully.")
