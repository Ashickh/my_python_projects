# s1={1,2,3,4}
# s2={3,4,5,6}
# for i in s1:
#     if i in s2:
#         print(i)


s1={1,2,3,4}
s2={3,4,5,6}

# union
print(s1.union(s2))

# intersection - common elements
print(s1.intersection(s2))

# s1-s2
print(s1.difference(s2))

# s2-s1
print(s2.difference(s1))