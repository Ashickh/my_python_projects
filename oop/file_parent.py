class Parent:
    def __init__(self,name,phone):
        self.name=name
        self.phone=phone
    def printpr(self):
        print(self.name,self.phone)
f=open('parent.txt','r')
for i in f:
    data=i.rstrip("\n").split(",")
    # print(data)
    name=data[0]
    phone=data[1]
    par=Parent(name,phone)
    par.printpr()
