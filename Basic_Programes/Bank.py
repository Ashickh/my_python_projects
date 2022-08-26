a = 100000
b = int (input ('enter the amount you want to withdraw'))


if b>a:
    print('Insufficient balance')
else:
    print ('Your current balance is', a - b)