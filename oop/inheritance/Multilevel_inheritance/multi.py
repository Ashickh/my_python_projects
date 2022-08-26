# multilevel/hierarchical

class A:
    def printa(self):
        print("inside A")
class B(A):
    def printb(self):
        print("inside B")
class C(B):
    def printc(self):
        print("inside C")
c=C()
c.printc()
c.printb()
c.printa()    # because class B is inheriting class A
