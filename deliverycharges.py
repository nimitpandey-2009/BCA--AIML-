amt=float(input("Enter your Order amount for calculate delivery Charges\n"))
premium=input("Are you have Premium membership (YES/NO)\n")
if premium=="YES":
    print("No Delivery Charges")
    print("Order Amount is", amt)
elif premium=="NO":
    if amt<=299:
        print("Delivery Charges = 50rs")
        charge=amt+50
        print("Total Order Amount is",charge)
    elif amt<=599:
         print("Delivery Charges = 30rs")
         charge=amt+30
         print("Total Order Amount is",charge)
    elif amt>=600:
        print("Delivery Charges = 00")
        print("Total Order Amount is",amt)
        