income=float(input("Enter Your Annual Income\n"))
if income <= 250000:
    print("No tax")
elif income <= 500000:
    print("tax:",(income - 250000)*0.05)
elif income <= 1000000:
    print("tax",12500+(income-500000)*0.2)
else:
    print("Tax",112500+(income-100000)*0.3)