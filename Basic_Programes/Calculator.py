# calculator
# select operation
# 1.add
# 2.sub
# 3.mul
# 4.div
# 5.stop
# enter num1
# enter num2
# print sum
# invalid


def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mult(a,b):
    return a*b
def div(a,b):
    return a/b

print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division")
print("Choose operation: ")
while True:
    op=int(input(""))
    if op in(1,2,3,4):
        num1=int(input("enter num1"))
        num2=int(input("enter num2"))
        if op==1:
            print("Answer is",add(num1,num2))
        elif op==2:
            print("Answer is",sub(num1,num2))
        elif op==3:
            print("Answer is",mult(num1,num2))
        elif op==4:
            print("Answer is",div(num1,num2))

    else:
        print("invalid operation")


