def change(f):
    def w(a,b):
        if a!="admin":
            raise Exception ("unauthorized access")
        else:
            return f(a,b)
    return w

@change
def changepassword(username,newpassword):
    mypassword=newpassword
    return mypassword
print(changepassword("admin",589248))