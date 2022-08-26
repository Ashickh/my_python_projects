e=(input("enter string"))
count={}                    # {"hello"
d=e.split()

for i in d:
    if i not in count:
        count.update({i:1})
    else:
        val=count[i]
        val+=1
        count.update({i:val})
print(count)

