balance=float(input("Enter Your Balance\n"))
amount=float(input("Enter Withrawal Amount\n"))
if amount>0:
    if amount<=balance:
        balance=balance-amount
        print("Withral Successful")
        print("Remaning Balance = ",balance)
    else:
        print("Insufficient Balance")
else:
    print("Invalid Withdrawal Amount")