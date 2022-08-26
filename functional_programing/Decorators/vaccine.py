def errorceation(func):
    def wrapper(a,b):
        if b<18:
            raise Exception("error")
        else:
            return func(a,b)
    return wrapper

@errorceation
def vaccine(name,age):
    return "successfully vaccinated"
print(vaccine("ashiq",20))






def errorcreate(function):
    def wrapper(a,b):
        if b<18:
            raise Exception("error")
        else:
            return function(a,b)
    return wrapper










