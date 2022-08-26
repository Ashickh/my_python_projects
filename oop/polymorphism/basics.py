# polymorphism = multiple forms

# method overloading  (python doesn't support overloading
# method overriding

# 1. Overloading

class A:
    def printa(self,num1):
        self.num1=num1
        print(self.num1)
class B:
    def printa(self,num1,num2):
        self.num1=num1
        self.num2=num2
        print(self.num1,self.num2)
b=B()
b.printa(5)      # will call method of class A
b.printa(5,10)   # will call method of class B