# fibonacci
# 0 1 1 2 3 5 8 13 21...
# print fist

# n1=0
# n2=1
# for i in range(10): # i=0, i=1, i=3...
#     print(n1)       # 0,1,1....9
#     nth=n1+n2       # 0+1=1(nth), 1+1=2(nth), 1+2=3(nth)...
#     n1=n2           # n1=1, n1=1, n1=2...
#     n2=nth          # n2=1, n2=2, n2=3...

# for i in range(2):      # 0,1
#     print(i)            # first loop(i=0) ,  second loop(i=1)
#     for j in range(5):  # 0,1,2,3,4
#         if i == 3:      # first and second loop- condition False
#             break       # didn't work
#         else:
#             print(j)    # first loop(j=0, j=1, j=2, j=3, j=4) return to i , second loop(j=0, j=1, j=2, j=3, j=4)

a=int(input("enter num1"))
b=int(input("enter num2"))
for i in range(a,b+1):
    print(a)
    nth=a+b
    a=b
    b=nth


