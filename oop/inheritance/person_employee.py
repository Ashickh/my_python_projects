class Vehicle:
    def setvehicle(self,name,brand):
        self.name=name
        self.brand=brand
        self.type=type
    def printvehicle(self):
        print(self.name,self.brand,self.type)
class Bus(Vehicle):
    def setbus(self,color,type,number):
        self.color=color
        self.type=type
        self.number=number
    def printbus(self):
        print(self.color,self.type,self.number,self.name,self.brand)
v1=Bus()
v1.setvehicle("Buses","Volvo",)
v1.setbus("White","Sleeper","KL44F1945")
v1.printbus()