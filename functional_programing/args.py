# *args

# def printelements(*args):     # can add any number of arguments
#     print(args)
# printelements(1,2,3,4,5,6)

# output will be in tuple with the name of variable declared after *

def sum(*args):
    sum=0
    for i in args:
        sum+=i
    print(sum)
sum(5,9)
sum(2,3,8,6,7)
