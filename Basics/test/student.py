class Student:
    def __init__(self, name, roll,dept,mark):
        self.name = name
        self.roll = roll
        self.dept=dept
        self.mark=mark
    def printpr(self):
        print (self.name, self.roll,self.dept,self.mark)

f = open ('student.txt', 'r')
for i in f:
    data = i.rstrip("\n").split(",")
    name = data[0]
    roll = data[1]
    dept = data[2]
    mark = data[3]

    # std = Student (name, roll,dept,mark)
    print(mark)
    print(max(Student))
    print(max(mark))



