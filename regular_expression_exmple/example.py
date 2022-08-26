# import re
# count=0
# matcher=re.finditer('ab','abaaaabccabccab')  # find count of 'ab' from second string
# # print(matcher)
# for i in matcher:
#     print(i.start())   # to find the starting indexes of matches
#     print(i.group())   # to find the group
#     count=count+1
# print(count)


import re
count=0
x='\W'
matcher=re.finditer(x,'avF #^&! jNb@1459')
# print(matcher)
for i in matcher:
    print(i.start())
    print(i.group())
    count=count+1
print("count=",count)