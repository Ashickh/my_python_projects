str="ABAABC"
x=""
for i in str:
    if i not in x:
        x+=i
    else:
        print(i)
        break


str="ABAABC"
x=""
y=""
for i in str:
    if i not in x:
        x+=i
    else:
        y+=i
print (y)













a=input("enter string")
x=""
for i in a:
    if i not in x:
        x=x+i
    else:
        print(i)
        break
