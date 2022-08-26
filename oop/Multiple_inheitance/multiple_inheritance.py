# multiple inheritance

class A:
    def printa(self):
        print("inside A")
class B:
    def printb(self):
        print("inside B")
class C(A,B):                # class C has two parent classes
    def printc(self):
        print("inside C")
c=C()
c.printa()
c.printb()
c.printc()