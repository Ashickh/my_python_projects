# employee class
# name
# id
# designation
# salary
# company

# self is used to point to the current instance

# instance variable- related to method.. and called using self
# static variable - related to class... and called using class name

class Employee:
    company_name="SBI Life"     # static variable
    def setemp(self,name,id,desig,salary):
        self.name=name
        self.id=id
        self.desig=desig
        self.salary=salary

    def printemp(self):
        print("Employee Name: ",self.name)
        print("Employee Id: ",self.id)
        print ("Employee Designation: ", self.desig)
        print ("Employee Salary: ", self.salary)
        print ("Employee Company Name: ", Employee.company_name)   # static variable called using class name
e1=Employee()
e1.setemp("Ashiq",41646,"Sr BDM",45000)
e1.printemp()

e2=Employee()
e2.setemp("Nizar",51596,"BDM",42000)
e2.printemp()

e3=Employee()
e3.setemp("Anas",49876,"Sr BDE",30000)
e3.printemp()