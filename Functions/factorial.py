def factorial(num):
    fact=1
    for i in range(1,num+1):
        fact*=i
    print(fact)
n=int(input("enter number"))
factorial(n)
factorial(5)



# n=int(input("enter number"))
# fact=1
# for i in range(1,n+1):
#     fact=fact*i
# print("factorial of",n,"=", fact)