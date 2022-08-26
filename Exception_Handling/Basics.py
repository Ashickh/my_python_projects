# exception handling
# exceptions= unexpected errors

num1=int(input("enter num1"))
num2=int(input("enter num2"))
print(num1/num2)            # 6/0 = error   zero division error

try:
    print("in try")
    print(num1/num2)      # try will work first
except Exception as a:
    print(a)
finally:
    print("in finally")    # finally always works


num1=int(input("enter num1"))
num2=int(input("enter num2"))
print(num1/num2)

try:
    print("in try")
    print(num1/num2)
except Exception as a:
    print(a)
finally:
    print("in finally")    # finally always works
