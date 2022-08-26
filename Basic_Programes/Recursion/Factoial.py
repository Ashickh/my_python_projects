def recfact(n):  # 5 4 3 2 1
    if n==1:     # n=5
        return n
    else:
        return n*recfact(n-1)
#              5*recmu
n=int(input("enter"))
print(recfact(n))