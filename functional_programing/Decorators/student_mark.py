def score(f):
    def stu(a,b):
        if b<50:
            raise Exception("Failed")
        else:
            return f(a,b)
    return stu
@score
def marks(name,mark):
    if mark>=50:
        print("Passed")

marks("hdgs",48)

