l=[5,7,1,6,8,2,4,3,9,]
e=int(input("enter number to search"))   # 5
l.sort()     # [1,2,3,4,5,6,7,8,9]
flag=0
low=0
upper=len(l)-1     # 9-1=8
while low<=upper:
    mid=(low+upper)//2   # (0+8)//2= 4   middle index is 4
    if l[mid]==e:
        flag=1
        break
    elif e>l[mid]:
        low=mid+1
    elif e<l[mid]:
        upper=mid-1
if flag==1:
    print("found")
else:
    print("not found")

