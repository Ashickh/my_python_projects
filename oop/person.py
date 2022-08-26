class Person:
    def setvalue(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def printvalue(self):
        print(self.name)
        print(self.age)
        print(self.place)
pe1=Person()
pe1.setvalue("Ashiq",27,"Kakkanad")
pe1.printvalue()

pe2=Person()
pe2.setvalue("Rinsha",26,"Kothamangalam")
pe2.printvalue()

z=Person()
z.setvalue("Zammu",2,"kochi")
z.printvalue()
