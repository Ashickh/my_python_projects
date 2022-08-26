class Person:
    def setvalue(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def printvalue(self):
        print(self.name,self.age,self.place)
class Student(Person):
    def setstd(self,roll,dept,school):
        self.roll=roll
        self.dept=dept
        self.school=school
    def printstd(self):
        print(self.roll,self.dept,self.school,self.name)  # "name" is a variable of class Person
st=Student()
st.setvalue("Ashiq",27,"Kakkanad")    # inheriting setvalue attribute from class Person
st.setstd(11,"BCA","IGC")
st.printstd()