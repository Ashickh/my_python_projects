# pyramid

#    *
#   * *
#  * * *
# * * * *


s=6
for i in range(5):
    for j in range(s):
        print(end=" ")
    s-=1
    for j in range(5):
        print("*",end=" ")
    print()

# inverted pyramid

# * * * *
#  * * *
#   * *
#    *

s=1
for i in range(4,0,-1):
    for j in range(s):
        print(end=" ")
    s+=1
    for j in range(i):
        print("*",end=" ")
    print()

# * * * *
#  * * * *
#   * * * *
#    * * * *

s=1
for i in range(5):
    for j in range(s):
        print(end=" ")
    s+=1
    for j in range(5):
        print("*",end=" ")
    print()
