age=int(input("Enter Your Age\n"))
if age>=18:
    test=input("Weather you have passed Driving test(yes/no)\n")
    if test=="yes":
        print("Your License is issued")
    else:
        print("Your License is not issued")
else:
    print("You are not eligible")