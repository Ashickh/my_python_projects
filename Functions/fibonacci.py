def fibonacci(nterms):
    n1=0
    n2=1
    for i in range(nterms):
        print(n1)
        nth=n1+n2
        n1=n2
        n2=nth
fibonacci(6)
