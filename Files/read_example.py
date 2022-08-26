f=open('example.txt','r')
# print(f)
for i in f:
    # print(i)   # there will be an extra line between the strings
    data=i.rstrip("\n")  # to remove that extra line
    print(data)