class Student:
    school_name="IGC"
    def setvalue(self,name,roll_no,dept):
        self.name=name
        self.roll_number=roll_no
        self.dept=dept

    def printvalue(self):
        print("Student name is",self.name)
        print("Roll Number is",self.roll_number)
        print("Department is",self.dept)
        print("School  name is",Student.school_name)
st1=Student()
st1.setvalue("Ashiq",1,"BCA")
st1.printvalue()

st2=Student()
st2.setvalue("Rinsha",2,"Bsc")
st2.printvalue()