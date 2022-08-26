# Mark=int(input("Eneter you Mark"))
# if Mark>100:
#     print("Invalid")
# elif Mark>80 and Mark<=89:
#     print('Your grade is A')
# elif Mark>=90 and Mark<=100:
#     print("Your grade is A+")
# elif Mark>=70 and Mark<=79:
#     print("Your grade is B+")
# elif Mark>=60 and Mark<=69:
#     print("Your grade is B")
# elif Mark>=50 and Mark<=59:
#     print("Your grade is C+")
#
# else:
#     print("Failed")

M=int(input("Enter Mark"))
if M<=100:
    if M>=90:    # nested if
        print("A+")
    elif M>=80:
        print("A")
    elif M>=70:
        print("B+")
    elif M>=60:
        print("B")
    elif M>=50:
        print("C+")
    else:
        print("Failed")
else:
    print("invalid")

