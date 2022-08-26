s="aeiou"
a=input("enter string")  # a
b=""
for i in a:
    if i not in s:   #l==a
        b+=i
print(b)

# s="abcdefghijklmnopqrstuvwxyz"
# a=input("enter string")  # a
# b=""
# for i in a:
#     if i in s:   #l==a
#         b+=i
# print(b)