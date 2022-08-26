class Person:
    def setvalue(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def printvalue(self):
        print(self.name)
        print(self.age)
        print(self.place)
    def __str__(self):
        return self.name+self.place+str(self.age)
pe1=Person()
pe1.setvalue("Ashiq",27,"Kakkanad")
print(pe1)