class Person:
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def printper(self):
        print(self.name,self.age,self.place)
class Parent(Person):
    def __init__(self,phone,address,name,age,place):
        super().__init__(name,age,place,)
        self.phone=phone
        self.address=address
    def printpar(self):
        print(self.phone,self.address)
class Employee(Parent):
    def __init__(self,id,desig,salary,name,age,place,phone,address):
        super().__init__(phone,address,name,age,place)
        self.id=id
        self.desig=desig
        self.salary=salary
    def printemp(self):
        print(self.id,self.desig,self.salary)
emp=Employee(41646,"bdm",40000,"ashiq",27,"kochi",859674856,"hhdgukdhjs")
emp.printemp()
emp.printpar()
emp.printper()