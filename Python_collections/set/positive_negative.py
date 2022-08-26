s={1,2,3,4,5,-1,-2,-3}   # positive
pos=set()
neg=set()
for i in s:
    if i>0:
        pos.add(i)
    else:
        neg.add(i)
print("positive elements are",(pos))
print("negative elements are",(neg))




