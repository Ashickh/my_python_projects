# overriding
# # child class method overrides parent class method
#
# class A:
#     def printa(self,num1):
#         self.num1=num1
#         print(self.num1,"inide A")
# class B(A):
#     def printa(self,no1):
#         self.no1=no1
#         print(self.no1,"inside B")
# b=B()
# b.printa(6)


class Books:
    def printa(self,name):
        self.name=name
        print(self.name,"Harry Potter")
class Library(Books):
    def printa(self,booknum):
        self.num=booknum
        print(self.num)
b=Library()
b.printa(122)  # method of child class overrides the methoad of parent class