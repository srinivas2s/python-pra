votes = ("A", "B", "A", "C", "B", "A", "A", "A")
d={}
for c in votes:
    if c in d:
        d[c]=d[c]+1
    else:
        d[c]=1
print('Votes = ',d)

max_votes = max(d.values())

for candidate in d:
    if d[candidate] == max_votes:
        print("Winner:", candidate)
        print("Votes:", max_votes)
f=open("file.txt", 'w')
f.write(str(d))
f.close()
