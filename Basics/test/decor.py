def valid(fun):
    def wrapper(a):
        if a!="+911294567890":
            raise Exception ("Not Valid")
        else:
            return fun(a)
    return wrapper

@valid
def change_number(phn_num):
    new_number=phn_num
    return new_number
print(change_number('+911294567890'))

#
# import  re
# string=input("enter number to validate")
# rule='^a[a-z]{3,8}a$'          # start and ends with a and small letters with min 3 and max 8
# matcher=re.fullmatch(rule,string)
# if matcher is not None:
#     print("valid")
# else:
#     print("invalid")