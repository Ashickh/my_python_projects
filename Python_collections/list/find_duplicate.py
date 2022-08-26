# l=[1,2,3,4,1,4,5,5]
# # dup=[]
# # for i in l:
# #     for j in range(i):
# #         if i==j:
# #          dup.append(i)
# # print(dup)

lst=[1,0,7,5,9,2,3,5,7,2,0,1,10]
newlist=[]
for i in lst:
    if i not in newlist:
        newlist.append(i)
print(newlist)








lst=[1,0,7,5,9,2,3,5,7,2,0,1,10]
newlist=[newlist.append(i) for i in lst if i not in newlist]
# newlist.append(i)
# print(newlist)
