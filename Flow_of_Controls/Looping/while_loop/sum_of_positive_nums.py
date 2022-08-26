ini=int(input("enter initial"))
fin=int(input("enter final"))
sum=0
while ini<=fin:
    if ini>0:
        sum=sum+ini
    ini+=1
print(sum)