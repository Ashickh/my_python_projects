# constructor
# constructor is used to initialise instance variables at the time of object creation

class Add:
    def __init__(self,num1,num2):    # __init__ is the constructor
        self.num1=num1
        self.num2=num2
    def printsum(self):
        print(self.num1+self.num2)
add1=Add(100,200)
add1.printsum()
