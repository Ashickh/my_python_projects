# prime number programe

# can devided by 1 or by the same number 1,3,5,7....

n=int(input("enter the number to check"))
flag=0
for i in range(2,n):
    if n%i==0:
        flag=1
        break
if flag==0:
    print("prime")
else:
    print("not prime")

