a = int (input ("enter initial"))
b = int (input ("enter final"))
sum = 0
for num in range (a, b + 1):  # 1
    for i in range (2, num):
        if num % i == 0:
            break
    else:
        sum = sum + num
print (sum)