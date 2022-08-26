# l=[3,6,1,7,8,2,4]
# l.sort()
# print(l)

# l=[3,6,1,7,8,2,4]
# newlist=[]
# while l:                     # 3,6,1,7...
#     minimum=l[0]            # minimum=3,
#     for i in l:
#         if i<minimum:       # 3<3.. 3<0(True)
#             minimum=i       # minimum=3,minimum=0
#     newlist.append(minimum) # newlist[0,..]
#     l.remove(minimum)       # 0 removed from l
# print(newlist[1])














list1=[4,9,1,8,7,2,3,5]
sor=[]
while list1:
    minimum=list1[0]
    for i in list1:
        if i<minimum:
            minimum=i
    sor.append(minimum)
    list1.remove(minimum)
print(sor)








