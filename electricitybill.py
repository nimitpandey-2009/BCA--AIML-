units=float(input("Enter Consumed Units to calculates the bill\n"))

if units>0:
    if units<=100:
        bill=units*5
    elif units<=200:
        bill=units*7
    else:
        bill=units*10
    if bill>2000:
        surcharges=bill*0.05
        bill=bill+surcharges
print("Total Electricity Bill is",bill)
        