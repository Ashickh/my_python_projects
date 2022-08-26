import re
rule='[+][9][1]\d{10}'
f=open('numbers.txt','r')
for i in f:
    data=i.rstrip("\n")
    # print(data)
    matcher=re.fullmatch(rule,data)
    if matcher is not None:
        print(data)




