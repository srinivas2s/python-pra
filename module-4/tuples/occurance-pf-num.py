data = (11, 2, 254, 33, 33, 344, 41,344)

d={}
for num in data:
    if num in d:
        d[num]+=1
    else:
        d[num]=1
print(d)

lst=[]
for num in data:
     l= len(str(num))
     lst.append((num,l))
print(lst)
