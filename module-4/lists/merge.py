
f1 = open("1.txt","r")
d1 = f1.read()
f1.close()

f2 = open("2.txt","r")
d2 = f2.read()
f2.close()

f3 = open("merge.txt","w")
f3.write(d1)
f3.write(" ")
f3.write(d2)
f3.close()

print("Merged Successfully")
