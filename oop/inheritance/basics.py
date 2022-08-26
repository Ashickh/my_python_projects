# inheritance
# child class have only one parent class - single inheritance

class A:                            # parent class/super class/base class
    def printa(self):
        print("inside A class")
class B(A):                         # inheriting class A,  child class/sub class/derived class
    def printb(self):
        print("inside B class")
b=B()
b.printb()
b.printa()                          # can call class A attribute in class B using inheritance
