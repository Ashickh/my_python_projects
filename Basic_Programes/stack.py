# data structures
# stack - Last In First Out (LIFO)

# using list will be easy in stack

# first set a size for the stack
# stack operations
# Add - (push)
# Remove - (pop)
# Display - (display)

stack=[]
size=int(input("enter size"))
top=0
def push():
    global top,size
    if top>=size:
        print("stack is full")
    else:
        e=int(input("enter element to add"))
        stack.append(e)
        top=top+1
        print(stack)
def pop():
    global top,size
    if top<=0:
        print("stack is empty")
    else:
        stack.pop()
        top=top-1
        print(stack)
while True:
    op=int(input("enter operation\n1. push\n2. pop"))
    if op==1:
        push()
    else:
        pop()

