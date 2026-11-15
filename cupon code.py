bill=float(input("Enter Bill Amount\n"))
if bill>500:
    code=input("Enter Coupon Code\n")
    if code=="SAVE10":
        dis=bill-(bill*0.1)
        print("Total Bill Amount=",dis)
    elif code=="SAVE20":
        dis=bill-(bill*0.2)
        print("Total Bill Amount=",dis)
    elif code!="SAVE10" or "SAVE20":
        print("Invalid Coupon")
else:
    print("Coupon cannot be used")
    print("Total bill Amount =",bill)