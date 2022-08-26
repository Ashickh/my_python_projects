class Person:
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def printper(self):
        print(self.name,self.age,self.place)
class Parent:
    def __init__(self,phone,address):
        self.phone=phone
        self.address=address
    def printpar(self):
        print(self.phone,self.address)
class Employee(Person,Parent):
    def __init__(self,id,desig,salary,name,age,place,phone,address):
        Person.__init__(self,name,age,place)
        Parent.__init__(self, phone,address)
        self.id=id
        self.desig=desig
        self.salary=salary
    def printemp(self):
        print(self.id,self.desig,self.salary)
emp=Employee(41646,"bdm",40000,"ashiq",27,"kochi",859674856,"hhdgukdhjs")
emp.printemp()
emp.printpar()
emp.printper()