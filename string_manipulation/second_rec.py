a=input("enter")
e=""
rec=""
for i in a:
    if i not in e:
        e+=i
    elif i not in rec:
        rec+=i
print(rec[1])
