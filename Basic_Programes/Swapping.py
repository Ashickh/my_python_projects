# method 1
# a=5
# b=10
# print('before swapping \n a is' ,a, '\n' ' b is' , b)
#
# a , b = b , a
# print('after swapping:')
# print('a is:', a, '\n' ' b is', b)


x = int(input('Enter value1'))
y = int(input('enter value2'))

print("before swapping \n x is", x,  '\n' ' y is', y)

# method 2
temp = x
x = y
y = temp

# method 3
# x = x + y
# y = x - y
# x = x - y
print('after swapping \n x is', x, '\n y is', y)

