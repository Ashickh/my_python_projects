#
# p=int(input("enter principle"))
# t=int(input("enter time"))
# r=float(input("enter rate"))
# ci=p(1+r/100)**t
# print(ci)
#
# ini=int(input('enter'))
# fin=int(input('enter'))
# sum=0
# for i in range(ini,fin+1):
#     if i%2==1:
#         sum+=i
# print(sum)

def fact(n):
    if n==1:
        return n
    else:
        return n*(fact(n-1))
print(fact(5))

# def fibonacci(n):
#     if n<=1:
#         return n
#     else:
#         return fibonacci(n-1)+fibonacci(n-2)
# nterms=int(input("enter"))
# for i in range(nterms):
#     print(fibonacci(i))
#





