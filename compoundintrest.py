p=float(input("Enter Your Principal Amount\n"))
r=float(input("Enter your rate of intrest\n"))
t=float(input("Enter Your Time in Year\n"))
CI=p*(1+(r/100))**t-p
print("Compound Intrest = ",CI)