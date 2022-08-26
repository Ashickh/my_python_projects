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
class Employee(Parent,Person):
    def setemp(self,id,desig,salary):
        self.id=id
        self.desig=desig
        self.salary=salary
    def printemp(self):
        print(self.id,self.desig,self.salary)
class Student(Employee):
    def setstud(self,roll,dept,score):
        self.roll=roll
        self.dept=dept
        self.score=score
    def printstud(self):
        print(self.roll,self.dept,self.score)
std=Student()
std.setper("Ashiq",27,"Kakkanad")
std.setpar(9544122514,"Kaimbanamkunnel")
std.setemp(41646,"BDM",45000)
std.setstud(4,"bca",856)
std.printper()
std.printpar()
std.printemp()
std.printstud()