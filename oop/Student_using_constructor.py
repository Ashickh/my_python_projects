class Student:
    School="Ilahia"
    def __init__(self,name,age,dept):
        self.name=name
        self.age=age
        self.dept=dept
    def printstd(self):
        print(self.name,self.age,self.dept,Student.School)
st1=Student("Ashiq",27,"MCA")
st1.printstd()
print(st1.name,st1.age,st1.School)   # we can print instance and static variables like this also
st2=Student("Rinsha",26,"Msc")
st2.printstd()