#
# def grade(mark):
#     if mark>100:
#         return "invalid"
#     elif mark>=90:
#         return "A+"
#     elif mark>=80:
#         return "A"
#     elif mark>=70:
#         return "B+"
#     elif mark>=60:
#         return "B"
#     else:
#         return "failed"
# m=int(input("enter mark"))
# print(grade(m))


# n1=0
# n2=1
# for i in range(10):
#     print(n1)
#     nth=n1+n2
#     n1=n2
#     n2=nth

# num1=int(input("enter initial"))
# num2=int(input("enter final"))
# sum=0
# for n in range(num1,num2+1):
#     for i in range(2,n):
#         if n%i==0:
#             break
#     else:
#         sum=sum+n
# print(sum)
#
# def add(a,b):
#     print(a+b)
# def sub(a,b):
#     print(a-b)
# def mul(a,b):
#     print(a*b)
# def div(a,b):
#     print(a/b)
# def expo(a,b):
#     print(a**b)
# def floor(a,b):
#     print(a//b)
#
# while True:
#     op = int (input ("select option\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Exponent\n6. Floor Division\n7. Stop"))
#     if op == 7:
#         break
#     elif op in (1, 2, 3, 4,5,6):
#         num1 = float (input ("enter num1"))
#         num2 = float (input ("enter num2"))
#         if op == 1:
#             add (num1, num2)
#         elif op == 2:
#             sub (num1, num2)
#         elif op == 3:
#             mul (num1, num2)
#         elif op == 4:
#             div (num1, num2)
#         elif op == 5:
#             expo (num1, num2)
#         elif op == 6:
#             floor (num1, num2)
#         else:
#             div (num1, num2)
#     else:
#         print ("invalid operation")

# s="aeiou"
# a=input("enter string")
# b=""
# for i in a:
#     if i not in s:
#         b+=i
# print(b)


p=5
for i in range(p):
    for j in range(i,p):
        print(" ",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()













