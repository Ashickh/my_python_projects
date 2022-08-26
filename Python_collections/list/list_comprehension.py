# list comprehension

# l=[1,2,5,7,9]
# square=[]         # can use when we use empty list programes
# for i in l:
#     square.append(i*i)
# print(square)
#
# l=[1,2,5,7,9]
# square=[i*i for i in l]
# print(square)

# l=[i for i in range(1,11)]
# print(l)
# l=[1,4,7,-7,-1]
# pos=[i for i in l if i>0]
# neg=[i for i in l if i<0]
# print("positive",pos,"negative",neg)


# 20 even numbers
listcompr=[i for i in range(1,100) if i%5==0]
print(listcompr)

# listcomp=[]
# for i in range(1,100):
#     if i%5==0:
#         listcomp.append(i)
# print(listcomp)



