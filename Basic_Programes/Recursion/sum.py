def recursivesum(n):
    if n==0:
        return n
    else:
        return n+recursivesum(n-1)
print(recursivesum(4))