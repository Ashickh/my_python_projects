class Student:
    def __init__(self, name, roll,mark):
        self.name = name
        self.roll = roll
        self.mark=mark
    def printpr(self):
        print (self.name, self.roll,self.mark)

f = open ('student.txt', 'r')
for i in f:
    data = i.rstrip("\n").split(",")
    name = data[0]
    roll = data[1]
    mark=data[2]
    par = Student (name, roll,mark)
    par.printpr ()
