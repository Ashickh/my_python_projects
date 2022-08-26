def add(a,b):
    print(a+b)
def sub(a,b):
    print(a-b)
def mul(a,b):
    print(a*b)
def div(a,b):
    print(a/b)

while True:
    op=int(input("select option\n1. Add\n2. Sub\n3. Mul\n4. Div\n5. Stop"))
    if op==5:
        break
    elif op in (1,2,3,4):
        num1=float(input("enter num1"))
        num2=float(input("enter num2"))
        if op==1:
            add(num1,num2)
        elif op==2:
            sub(num1,num2)
        elif op==3:
            mul(num1,num2)
        else:
            div(num1,num2)
    else:
        print("invalid operation")