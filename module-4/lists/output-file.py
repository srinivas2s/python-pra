
file = open("ip.txt", "r")
lines = file.readlines()
file.close()


outfile = open("output.txt", "w")
for i in range(len(lines)):
    if i % 2 == 0:
        outfile.write(lines[i])
outfile.close()
print("Odd-numbered lines copied successfully.")
