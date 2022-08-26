class Animal:
    def __init__(self,name,type):
        self.name=name
        self.type=type
    def printanimal(self):
        print(self.name,self.type)
class Dog(Animal):
    def __init__(self,breed,color,name,type):
        super().__init__(name,type)
        self.breed=breed
        self.color=color
    def printdog(self):
        print(self.breed,self.color,self.name,self.type)
d1=Dog("bomaranian","brown","jack","Pets")
d1.printdog()
d1.printanimal()
