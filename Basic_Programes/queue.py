# queue

# add  - enqueue
# remove  -  dequeue
# display

# queue=[]
# size=int(input("enter size"))
# top=0
# def enqueue():
#     global top,size
#     if top>=size:
#         print("queue is full")
#     else:
#         e=int(input("enter elements to add"))
#         queue.append(e)
#         top=top+1
#         print(queue)
# def dequeu():
#     global top,size
#     if top<=0:
#         print("queue is empty")
#     else:
#         queue.remove(queue[0])
#         top=top-1
#         print(queue)
# while True:
#     op=int(input("choose operation\n1. enqueue\n2. dequeue\n3. stop"))
#
#     if op==1:
#         enqueue()
#
#     else:
#         dequeu()


queue=[]
size=int(input("enter size"))
top=0
def enqueue():
    global top,size
    if top>=size:
        print("queue is full")
    else:
        e=int(input("enter element"))
        queue.append(e)
        top+=1
        print(queue)
def dequeue():
    global top,size
    if top<=0:
        print("queue is empty")
    else:
        queue.remove(queue[0])
        top-=1
        print(queue)
while True:
    op=int(input("choose option\n1. enqueue\n2. dequeue\n3. stop"))
    if op==3:
        break
    elif op==1:
        enqueue()
    else:
        dequeue()

# ini=int(input("iniial"))
# fin=int(input("enter final"))
#
# for num in range(ini,fin+1):
#     for i in range(2,num):
#         if num%i==0:
#             break
#     else:
#         print(num)













