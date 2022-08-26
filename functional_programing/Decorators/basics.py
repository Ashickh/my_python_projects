def changevalue(function):                  # function=sub
    def wrapper(a,b):                       # a=4, b=6
        if a>=b:
            return function(a,b)
        else:
            a,b=b,a                         # a=6, b=4
            return function(a,b)
    return wrapper

@changevalue
def sub(n1,n2):
    return n1-n2
print(sub(9,6))