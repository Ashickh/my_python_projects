s={2,3,5,8,9,11,14}
odd=set()
even=set()
for i in s:
    if i%2==0:
        even.add(i)
    else:
        odd.add(i)
print("even elements are",(even))   # odd
print("odd elements are",(odd))     # even

