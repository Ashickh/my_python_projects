# for else

# a=4
# for i in range(5):
#     if i==a:
#         print(i)
#         break
# else:
#     print("in else")

# prime number using for else

n=int(input("enter number"))
for i in range(2,n):
    if n%i==0:
        print("not prime")
        break
else:
    print("prime")

