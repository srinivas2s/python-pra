orders = [
    ("O1","Ram",1000),
    ("O2","Ravi",5000),
    ("O3","Sam",2000),
    ("O4","John",4000)
]

total = sum(order[2] for order in orders)

avg = total/len(orders)

print("Total =", total)
print("Average =", avg)

top2 = sorted(orders, key=lambda x:x[2], reverse=True)[:2]

print("Top 2 Orders:")
for i in top2:
    print(i)