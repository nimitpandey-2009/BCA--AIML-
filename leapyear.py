y=int(input("Enter Your Year\n"))
if y%100==0:
    if y%400==0:
        print("Leap year")
    else:
        print("Non-leap Year")
else:
    if y%4==0:
        print("Leap year")
    else:
        print("Non-leap Year")