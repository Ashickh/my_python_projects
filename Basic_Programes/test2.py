# a=int(input("enter num1"))
# b=int(input("enter num2"))
# for num in range(a,b+1):
#     for i in range(2,num):
#         if num%i==0:
#             break


# l=[1,6,4,2,3,4,7,1]
# print(list(set(l)))

#
# a=int(input('enter num1'))
# flag=0
# for i in range(2,a):
#     if a%i==0:
#         flag=1
#         break
# if flag==0:
#     print("prime")
# else:
#     print("not")

# stack=[]
# size=int(input("enter size"))
# top=0
# def push():
#     global top,size
#     if top>=size:
#         print("stack is full")
#     else:
#         e=int(input("enter element"))
#         stack.append(e)
#         top=top+1
#         print(stack)
# def pop():
#     global top,size
#     if top<=0:
#         print("stack is empty")
#     else:
#         stack.pop()
#         top-=1
#         print(stack)
# while True:
#     a=int(input("operation\n1.push\n2.pop"))
#     if a==1:
#         push()
#     else:
# #         pop()
#
# queue=[]
# size=int(input('size'))
# top=0
# def enqueue():
#     global top,size
#     if top>=size:
#         print("full")
#     else:
#         e=int(input("element"))
#         queue.append(e)
#         top+=1
#         print(queue)
# def dequeue():
#     global top,size
#     if top<=0:
#         print("empty")
#     else:
#         queue.remove(queue[0])
#         top-=1
#         print(queue)
#
# while True:
#     a=int(input("op\n1.enq\n2.deq"))
#     if a==1:
#         enqueue()
#     else:
#         dequeue()

#
# # n=5
#
#     print()

n= int(input("enter number"))
if n%2!=0:
    print("Wierd")
elif n%2==0:
    if n in range(2,5):
        print("not wierd")










