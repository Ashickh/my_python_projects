# find second minimum
# lst=[3,5,7,9,0,8,55,34,23,76,4,65,12,89,56,76,34,289,49,12,63,976]
# newlist=[]
# while lst:
#     minimum=lst[0]
#     for i in lst:
#         if i<minimum:
#             minimum=i
#     newlist.append(minimum)
#     lst.remove(minimum)
# print("second minimum is",newlist[1])


# # patterns
# for i in range(6):
#     for j in range(i):
#         print("1",end=" ")
#     print()
# for i in range(5,0,-1):
#     for j in range(i):
#         print("2",end=" ")
#     print()
#
# for i in range(6):
#     for j in range(i):
#         print("3",end=" ")
#     print()
# for i in range(5,0,-1):
#     for j in range(i):
#         print("4",end=" ")
#     print()

# remove middle element

# b=[3,77,0,5,33,6,22,5,90,32,56,78,98,54,67,11,34,88]
# print(len(b)//2)  # middle element's index is 9
# b.pop(9)
# print(b)

# print(4+3%5)


def mult(*args):
    result=1
    for nums in args:
        result=result*nums
    print(result)
mult(2,4)
mult(2,4,9)