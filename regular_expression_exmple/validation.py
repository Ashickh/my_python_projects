# import re
# phone=input("enter number to validate")
# rule='[+][9][1]\d{10}'               # mobile number validation
# matcher=re.fullmatch(rule,phone)
# if matcher is not None:
#     print("valid")
# else:
#     print("invalid")


# import  re          # number plate validation
# plate=input("enter number to validate")
# rule='[K][L]\d{2}[A-Z]{1,2}\d{4}'
# matcher=re.fullmatch(rule,plate)
# if matcher is not None:
#     print("valid")
# else:
#     print("invalid")

# import  re
# string=input("enter number to validate")
# rule='^a[\w\W]*b$'                        # start with a ends with b  in between n no.of numbes and special chars
# matcher=re.fullmatch(rule,string)
# if matcher is not None:
#     print("valid")
# else:
#     print("invalid")

# import  re          # start with 2 nos. followed by special chars (minimum 1 sp chars)
# string=input("enter number to validate")
# rule='[0-9]{2}\W+'
# matcher=re.fullmatch(rule,string)
# if matcher is not None:
#     print("valid")
# else:
#     print("invalid")

# import  re          # numbers and cap letters with min 3 max 8
# string=input("enter number to validate")
# rule='[0-9A-Z]{3,8}'
# matcher=re.fullmatch(rule,string)
# if matcher is not None:
#     print("valid")
# else:
#     print("invalid")

# import  re
# string=input("enter number to validate")
# rule='^a[a-z]{3,8}a$'          # start and ends with a and small letters with min 3 and max 8
# matcher=re.fullmatch(rule,string)
# if matcher is not None:
#     print("valid")
# else:
#     print("invalid")

# import  re
# string=input("enter number to validate")
# rule='[A-Z]+[\W\d]$'          # ends with one number or sp char
# matcher=re.fullmatch(rule,string)
# if matcher is not None:
#     print("valid")
# else:
#     print("invalid")

# import  re    # mail validation
# string=input("enter number to validate")
# rule='[a-z0-9._]+[@][a-z]+[.][comin]{2,3}'
# matcher=re.fullmatch(rule,string)
# if matcher is not None:
#     print("valid")
# else:
#     print("invalid")



import  re
string=input("enter string to validate")
rule='^[A-Z]\w{5,10}[A-Z]$'
matcher=re.fullmatch(rule,string)
if matcher is not None:
    print("valid")
else:
    print("invalid")