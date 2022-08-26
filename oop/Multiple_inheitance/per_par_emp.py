class Person:
    def setper(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def printper(self):
        print(self.name,self.age,self.place)
class Parent:
    def setpar(self,phone,address):
        self.phone=phone
        self.address=address
    def printpar(self):
        print(self.phone,self.address)
class Employee(Person,Parent):
    def setemp(self,id,desig,salary):
        self.id=id
        self.desig=desig
        self.salary=salary
    def printemp(self):
        print(self.id,self.desig,self.salary)
emp=Employee()
emp.setper("Ashiq",27,"Kakkanad")
emp.setpar(9544122514,"Kaimbanamkunnel")
emp.setemp(41646,"BDM",45000)
emp.printper()
emp.printpar()
emp.printemp()